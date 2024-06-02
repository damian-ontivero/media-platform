from src.contexts.backoffice.series.domain.serie import Serie
from src.contexts.backoffice.series.domain.serie_repository import SerieRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .create_command import SerieCreateCommand


class SerieCreateCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return SerieCreateCommand

    def handle(self, command: SerieCreateCommand) -> None:
        serie = Serie.create(command.title, command.seasons)
        self._repository.save(serie)
