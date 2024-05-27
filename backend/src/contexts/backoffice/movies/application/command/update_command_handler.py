from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain import NotFound
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .update_command import MovieUpdateCommand


class MovieUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return MovieUpdateCommand

    def handle(self, command: MovieUpdateCommand) -> None:
        movie = self._repository.search(command.id)
        if movie is None:
            raise NotFound(f"Movie: {command.id!r} not found")
        movie.update(command.title, command.media_id)
        self._repository.save(movie)
