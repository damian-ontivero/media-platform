from src.contexts.backoffice.movies.domain import MovieAlreadyExists, MovieDoesNotExist, MovieRepository
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus
from src.contexts.shared.domain.bus.query import QueryBus
from src.contexts.shared.domain.criteria import Criteria

from .update_command import MovieUpdateCommand


class MovieUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return MovieUpdateCommand

    async def handle(self, command: MovieUpdateCommand) -> None:
        movie = self._repository.search(command.id)
        if movie is None:
            raise MovieDoesNotExist(f"Movie with id {command.id!r} does not exist")
        self._ensure_title_is_available(command)
        self._ensure_media_is_available(command)
        movie.update(command.title, command.media_id)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())

    def _ensure_title_is_available(self, command: MovieUpdateCommand) -> None:
        criteria = Criteria.from_primitives(
            filter={
                "conjunction": "AND",
                "conditions": [
                    {"field": "id", "operator": "NOT_EQUALS", "value": command.id},
                    {"field": "title", "operator": "EQUALS", "value": command.title},
                ],
            },
            sort=None,
            page_size=None,
            page_number=None,
        )
        movies = self._repository.matching(criteria)
        if movies:
            raise MovieAlreadyExists("A movie with the same title already exists")

    async def _ensure_media_is_available(self, command: MovieUpdateCommand) -> None:
        await self._query_bus.ask(MediaFindByIdQuery(command.media_id))
