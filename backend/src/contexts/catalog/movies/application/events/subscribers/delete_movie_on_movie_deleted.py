from src.contexts.backoffice.movies.domain.movie_events import MovieDeletedDomainEvent
from src.contexts.catalog.movies.application.services.movie_deleter import MovieDeleter
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DeleteMovieOnMovieDeleted(DomainEventSubscriber):
    def __init__(self, deleter: MovieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MovieDeletedDomainEvent]

    async def on(self, event: MovieDeletedDomainEvent) -> None:
        await self._deleter.run(event.movie_id)
