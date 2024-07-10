from src.contexts.backoffice.movies.domain import Movie, MovieAlreadyExists, MovieRepository
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.bus.query import QueryBus
from src.contexts.shared.domain.criteria import Criteria


class MovieCreator:
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, title: str, media_id: str) -> None:
        self._ensure_title_is_available(title)
        await self._ensure_media_is_available(media_id)
        movie = Movie.create(title, media_id)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())

    def _ensure_title_is_available(self, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": title}]},
            sort=None,
            page_size=None,
            page_number=None,
        )
        title = self._repository.matching(criteria)
        if title:
            raise MovieAlreadyExists("A movie with the same title already exists")

    async def _ensure_media_is_available(self, media_id: str) -> None:
        await self._query_bus.ask(MediaFindByIdQuery(media_id))
