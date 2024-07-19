from src.contexts.backoffice.movies.application.commands.movie_create_command import MovieCreateCommand
from src.contexts.backoffice.movies.application.services.movie_creator import MovieCreator
from src.contexts.shared.domain.command_bus.command import Command
from src.contexts.shared.domain.command_bus.command_handler import CommandHandler


class MovieCreateCommandHandler(CommandHandler):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> Command:
        return MovieCreateCommand

    async def handle(self, command: MovieCreateCommand) -> None:
        await self._creator.run(command.title, command.media_id)
