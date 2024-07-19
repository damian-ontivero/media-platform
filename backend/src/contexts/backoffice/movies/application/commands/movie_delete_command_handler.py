from src.contexts.backoffice.movies.application.commands.movie_delete_command import MovieDeleteCommand
from src.contexts.backoffice.movies.application.services.movie_deleter import MovieDeleter
from src.contexts.shared.domain.command_bus.command import Command
from src.contexts.shared.domain.command_bus.command_handler import CommandHandler


class MovieDeleteCommandHandler(CommandHandler):
    def __init__(self, deleter: MovieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> Command:
        return MovieDeleteCommand

    async def handle(self, command: MovieDeleteCommand) -> None:
        await self._deleter.run(command.id)
