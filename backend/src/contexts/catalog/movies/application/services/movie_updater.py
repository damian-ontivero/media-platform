from src.contexts.catalog.movies.domain.movie_repository import MovieRepository
from src.contexts.catalog.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from src.contexts.shared.domain.event_bus.event_bus import EventBus
from src.contexts.shared.domain.query_bus.query_bus import QueryBus


class MovieUpdater:
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, id: str, title: str, media_id: str) -> None:
        media = await self._query_bus.ask(MediaFindByIdQuery(media_id))
        movie = self._repository.search(id)
        movie.update(title, media.duration)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())
