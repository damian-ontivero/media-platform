from src.contexts.backoffice.movies.domain.movie_events import MovieCreatedDomainEvent
from src.contexts.catalog.movies.application.services.movie_finder import MovieFinder
from src.contexts.catalog.movies.domain import Movie, MovieRepository
from src.contexts.shared.domain import DomainEvent, DomainEventSubscriber
from src.contexts.shared.domain.bus.event import EventBus


class CreateMovieOnMovieCreated(DomainEventSubscriber):
    def __init__(self, repository: MovieRepository, finder: MovieFinder, event_bus: EventBus) -> None:
        self._repository = repository
        self._finder = finder
        self._event_bus = event_bus

    def subscribed_to(self) -> list[DomainEvent]:
        return [MovieCreatedDomainEvent]

    async def on(self, event: MovieCreatedDomainEvent) -> None:
        media = self._finder.run(event.media_id)
        movie = Movie.create(event.title, media.duration)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())
