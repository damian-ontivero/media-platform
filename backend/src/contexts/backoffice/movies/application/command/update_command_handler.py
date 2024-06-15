from src.contexts.backoffice.movies.domain import MovieDoesNotExist, MovieRepository
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.query import QueryBus

from .update_command import MovieUpdateCommand


class MovieUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository, query_bus: QueryBus) -> None:
        self._repository = repository
        self._query_bus = query_bus

    def subscribed_to(self) -> Command:
        return MovieUpdateCommand

    def handle(self, command: MovieUpdateCommand) -> None:
        self._ensure_media_exists(command.media_id)
        movie = self._repository.search(command.id)
        if movie is None:
            raise MovieDoesNotExist(f"Movie with id {command.id!r} does not exist")
        movie.update(command.title, command.media_id)
        self._repository.save(movie)

    def _ensure_media_exists(self, media_id: str) -> None:
        self._query_bus.ask(MediaFindByIdQuery(media_id))
