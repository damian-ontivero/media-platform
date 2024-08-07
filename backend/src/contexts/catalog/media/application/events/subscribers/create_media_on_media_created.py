from src.contexts.backoffice.media.domain.media_events import MediaCreatedDomainEvent
from src.contexts.catalog.media.application.services.media_creator import MediaCreator
from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class CreateMediaOnMediaCreated(DomainEventSubscriber):
    def __init__(self, creator: MediaCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> list[DomainEvent]:
        return [MediaCreatedDomainEvent]

    async def on(self, event: MediaCreatedDomainEvent) -> None:
        await self._creator.run(event.title, event.size, event.duration, event.path)
