from src.contexts.backoffice.movies.domain.movie_exceptions import MovieAlreadyExists, MovieDoesNotExist
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from src.contexts.shared.domain.criteria.criteria import Criteria
from src.contexts.shared.domain.event_bus.event_bus import EventBus
from src.contexts.shared.domain.query_bus.query_bus import QueryBus


class MovieUpdater:
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, id: str, title: str, media_id: str) -> None:
        movie = self._repository.search(id)
        if movie is None:
            raise MovieDoesNotExist(f"Movie with id {id!r} does not exist")
        self._ensure_title_is_available(id, title)
        await self._ensure_media_is_available(media_id)
        movie.update(title, media_id)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())

    def _ensure_title_is_available(self, id: str, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={
                "conjunction": "AND",
                "conditions": [
                    {"field": "id", "operator": "NOT_EQUALS", "value": id},
                    {"field": "title", "operator": "EQUALS", "value": title},
                ],
            },
            sort=None,
            page_size=None,
            page_number=None,
        )
        exists = self._repository.matching(criteria)
        if exists:
            raise MovieAlreadyExists("A movie with the same title already exists")

    async def _ensure_media_is_available(self, media_id: str) -> None:
        await self._query_bus.ask(MediaFindByIdQuery(media_id))
