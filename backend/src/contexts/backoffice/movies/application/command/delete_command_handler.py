from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain import EntityNotFound
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .delete_command import MovieDeleteCommand


class MovieDeleteCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return MovieDeleteCommand

    def handle(self, command: MovieDeleteCommand) -> None:
        movie = self._repository.search(command.id)
        if movie is None:
            raise EntityNotFound(f"Movie: {command.id!r} not found")
        self._repository.delete(command.id)
