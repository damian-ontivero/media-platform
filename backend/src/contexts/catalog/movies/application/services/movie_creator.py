from src.contexts.catalog.movies.domain import Movie, MovieRepository
from src.contexts.catalog.shared.media.application.queries import MediaFindByIdQuery
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.bus.query import QueryBus


class MovieCreator:
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, title: str, media_id: str) -> None:
        media = await self._query_bus.ask(MediaFindByIdQuery(media_id))
        movie = Movie.create(title, media.duration)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())
