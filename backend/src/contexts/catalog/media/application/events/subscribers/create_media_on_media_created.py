from src.contexts.backoffice.media.domain.media_events import MediaCreatedDomainEvent
from src.contexts.catalog.media.domain import Media, MediaRepository
from src.contexts.catalog.shared.media.application.queries import MediaFindByIdQuery
from src.contexts.shared.domain import DomainEvent, DomainEventSubscriber
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.bus.query import QueryBus


class CreateMediaOnMediaCreated(DomainEventSubscriber):
    def __init__(self, repository: MediaRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    def subscribed_to(self) -> list[DomainEvent]:
        return [MediaCreatedDomainEvent]

    async def on(self, event: MediaCreatedDomainEvent) -> None:
        media = await self._query_bus.ask(MediaFindByIdQuery(event.media_id))
        media = Media.create(event.title, media.duration)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())
