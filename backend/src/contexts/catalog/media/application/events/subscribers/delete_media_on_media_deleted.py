from src.contexts.catalog.media.application.services.media_deleter import MediaDeleter
from src.contexts.backoffice.media.domain.media_events import MediaDeletedDomainEvent
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DeleteMediaOnMediaDeleted(DomainEventSubscriber):
    def __init__(self, deleter: MediaDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MediaDeletedDomainEvent]

    async def on(self, event: MediaDeletedDomainEvent) -> None:
        await self._deleter.run(event.media_id)
