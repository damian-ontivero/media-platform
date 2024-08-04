from src.contexts.catalog.series.application.services.serie_updater import SerieUpdater
from src.contexts.backoffice.series.domain.serie_events import SerieUpdatedDomainEvent
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class UpdateSerieOnSerieUpdated(DomainEventSubscriber):
    def __init__(self, updater: SerieUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [SerieUpdatedDomainEvent]

    async def on(self, event: SerieUpdatedDomainEvent) -> None:
        await self._updater.run(event.id, event.title, event.seasons)
