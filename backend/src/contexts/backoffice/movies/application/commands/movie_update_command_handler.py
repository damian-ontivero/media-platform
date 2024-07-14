from src.contexts.backoffice.movies.application.services import MovieUpdater
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .movie_update_command import MovieUpdateCommand


class MovieUpdateCommandHandler(CommandHandler):
    def __init__(self, updater: MovieUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> Command:
        return MovieUpdateCommand

    async def handle(self, command: MovieUpdateCommand) -> None:
        await self._updater.run(command.id, command.title, command.media_id)
