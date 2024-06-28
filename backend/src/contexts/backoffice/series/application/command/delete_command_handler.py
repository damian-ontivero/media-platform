from src.contexts.backoffice.series.domain import SerieDeleted, SerieDoesNotExist, SerieRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus

from .delete_command import SerieDeleteCommand


class SerieDeleteCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return SerieDeleteCommand

    def handle(self, command: SerieDeleteCommand) -> None:
        serie = self._repository.search(command.id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {command.id!r} does not exist")
        self._repository.delete(command.id)
        self._event_bus.publish(SerieDeleted.create({"id": command.id}))
