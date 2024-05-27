from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .create_command import MovieCreateCommand


class MovieCreateCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return MovieCreateCommand

    def handle(self, command: MovieCreateCommand) -> None:
        movie = Movie.create(command.title, command.media_id)
        self._repository.save(movie)
