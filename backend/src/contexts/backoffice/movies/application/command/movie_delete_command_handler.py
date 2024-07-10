from src.contexts.backoffice.movies.application.services import MovieDeleter
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .movie_delete_command import MovieDeleteCommand


class MovieDeleteCommandHandler(CommandHandler):
    def __init__(self, deleter: MovieDeleter) -> None:
        self._deleter = deleter

    def subscribed_to(self) -> Command:
        return MovieDeleteCommand

    async def handle(self, command: MovieDeleteCommand) -> None:
        await self._deleter.run(command.id)
