from src.contexts.catalog.series.application.services.serie_deleter import SerieDeleter
from src.contexts.backoffice.series.domain.serie_events import SerieDeletedDomainEvent
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DeleteSerieOnSerieDeleted(DomainEventSubscriber):
    def __init__(self, deleter: SerieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [SerieDeletedDomainEvent]

    async def on(self, event: SerieDeletedDomainEvent) -> None:
        await self._deleter.run(event.serie_id)
