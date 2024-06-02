from src.contexts.backoffice.series.domain.serie_repository import SerieRepository
from src.contexts.shared.domain import EntityNotFound
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
            raise EntityNotFound(f"Serie: {command.id!r} not found")
        self._repository.delete(command.id)
