from src.contexts.backoffice.movies.application.commands.movie_update_command import MovieUpdateCommand
from src.contexts.backoffice.movies.application.services.movie_updater import MovieUpdater
from src.contexts.shared.domain.command_bus.command import Command
from src.contexts.shared.domain.command_bus.command_handler import CommandHandler


class MovieUpdateCommandHandler(CommandHandler):
    def __init__(self, updater: MovieUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> Command:
        return MovieUpdateCommand

    async def handle(self, command: MovieUpdateCommand) -> None:
        await self._updater.run(command.id, command.title, command.media_id)
