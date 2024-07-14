from src.contexts.backoffice.series.domain.serie_events import SerieCreatedDomainEvent
from src.contexts.catalog.series.application.services.serie_finder import SerieFinder
from src.contexts.catalog.series.domain import Serie, SerieRepository
from src.contexts.shared.domain import DomainEvent, DomainEventSubscriber
from src.contexts.shared.domain.bus.event import EventBus


class CreateSerieOnSerieCreated(DomainEventSubscriber):
    def __init__(self, repository: SerieRepository, finder: SerieFinder, event_bus: EventBus) -> None:
        self._repository = repository
        self._finder = finder
        self._event_bus = event_bus

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [SerieCreatedDomainEvent]

    async def on(self, event: SerieCreatedDomainEvent) -> None:
        media = self._finder.run(event.media_id)
        serie = Serie.create(event.title, media.duration)
        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_domain_events())
