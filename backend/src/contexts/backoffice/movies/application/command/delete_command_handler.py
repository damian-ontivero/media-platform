from src.contexts.backoffice.movies.domain import MovieDoesNotExist, MovieRepository
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
            raise MovieDoesNotExist(f"Movie with id {command.id!r} does not exist")
        self._repository.delete(command.id)
