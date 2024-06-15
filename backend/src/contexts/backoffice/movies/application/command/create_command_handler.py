from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.query import QueryBus

from .create_command import MovieCreateCommand


class MovieCreateCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository, query_bus: QueryBus) -> None:
        self._repository = repository
        self._query_bus = query_bus

    def subscribed_to(self) -> Command:
        return MovieCreateCommand

    def handle(self, command: MovieCreateCommand) -> None:
        self._ensure_media_exists(command.media_id)
        movie = Movie.create(command.title, command.media_id)
        self._repository.save(movie)

    def _ensure_media_exists(self, media_id: str) -> None:
        self._query_bus.ask(MediaFindByIdQuery(media_id))
