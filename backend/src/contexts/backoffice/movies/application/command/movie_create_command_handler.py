from src.contexts.backoffice.movies.application.services import MovieCreator
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .movie_create_command import MovieCreateCommand


class MovieCreateCommandHandler(CommandHandler):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    def subscribed_to(self) -> Command:
        return MovieCreateCommand

    async def handle(self, command: MovieCreateCommand) -> None:
        await self._creator.run(command.title, command.media_id)
