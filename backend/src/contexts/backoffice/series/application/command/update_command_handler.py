from src.contexts.backoffice.series.domain import SerieDoesNotExist, SerieRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .update_command import SerieUpdateCommand


class SerieUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return SerieUpdateCommand

    def handle(self, command: SerieUpdateCommand) -> None:
        serie = self._repository.search(command.id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {command.id!r} does not exist")
        serie.update(command.title, command.seasons)
        self._repository.save(serie)
