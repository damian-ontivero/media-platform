from src.contexts.backoffice.media.domain.media_events import MediaCreatedDomainEvent
from src.contexts.catalog.media.domain.media import Media
from src.contexts.catalog.media.domain.media_repository import MediaRepository
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from src.contexts.shared.domain.event_bus.event_bus import EventBus


class CreateMediaOnMediaCreated(DomainEventSubscriber):
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MediaCreatedDomainEvent]

    async def on(self, event: MediaCreatedDomainEvent) -> None:
        media = Media.create(event.title, media.duration)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())
