from src.contexts.backoffice.movies.domain import MovieCreatedDomainEvent
from src.contexts.catalog.movies.domain import Movie, MovieRepository
from src.contexts.catalog.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain import DomainEvent, DomainEventSubscriber
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.bus.query import QueryBus


class CreateMovieOnMovieCreated(DomainEventSubscriber):
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    def subscribed_to(self) -> list[DomainEvent]:
        return [MovieCreatedDomainEvent]

    async def on(self, event: MovieCreatedDomainEvent) -> None:
        media = await self._query_bus.ask(MediaFindByIdQuery(event.media_id))
        movie = Movie.create(event.title, media.duration)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())
