from src.contexts.backoffice.movies.domain.movie_events import MovieUpdatedDomainEvent
from src.contexts.catalog.movies.application.services.movie_updater import MovieUpdater
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class UpdateMovieOnMovieUpdated(DomainEventSubscriber):
    def __init__(self, update: MovieUpdater) -> None:
        self._update = update

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MovieUpdatedDomainEvent]

    async def on(self, event: MovieUpdatedDomainEvent) -> None:
        await self._update.run(event.id, event.title, event.media_id)
