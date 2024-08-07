from src.contexts.backoffice.movies.domain.movie_events import MovieCreatedDomainEvent
from src.contexts.catalog.movies.application.services.movie_creator import MovieCreator
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class CreateMovieOnMovieCreated(DomainEventSubscriber):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MovieCreatedDomainEvent]

    async def on(self, event: MovieCreatedDomainEvent) -> None:
        await self._creator.run(event.title, event.media_id)
