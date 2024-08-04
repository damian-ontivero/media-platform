from src.contexts.catalog.media.application.services.media_updater import MediaUpdater
from src.contexts.backoffice.media.domain.media_events import MediaUpdatedDomainEvent
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class UpdateMediaOnMediaUpdated(DomainEventSubscriber):
    def __init__(self, updater: MediaUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MediaUpdatedDomainEvent]

    async def on(self, event: MediaUpdatedDomainEvent) -> None:
        await self._updater.run(event.id, event.title, event.size, event.duration, event.path)
