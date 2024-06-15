from src.contexts.backoffice.series.domain import SerieDoesNotExist, SerieRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .delete_command import SerieDeleteCommand


class SerieDeleteCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return SerieDeleteCommand

    def handle(self, command: SerieDeleteCommand) -> None:
        serie = self._repository.search(command.id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {command.id!r} does not exist")
        self._repository.delete(command.id)
