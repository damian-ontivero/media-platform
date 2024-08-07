from src.contexts.backoffice.series.domain.serie_events import SerieCreatedDomainEvent
from src.contexts.catalog.series.application.services.serie_creator import SerieCreator
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class CreateSerieOnSerieCreated(DomainEventSubscriber):
    def __init__(self, creator: SerieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [SerieCreatedDomainEvent]

    async def on(self, event: SerieCreatedDomainEvent) -> None:
        await self._creator.run(event.title, event.seasons)
