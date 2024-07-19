from src.contexts.backoffice.media.domain.media_events import MediaDeletedDomainEvent
from src.contexts.backoffice.media.domain.media_exceptions import MediaDoesNotExist
from src.contexts.backoffice.media.domain.media_repository import MediaRepository
from src.contexts.shared.domain.event_bus.event_bus import EventBus


class MediaDeleter:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str) -> None:
        media = self._repository.search(id)
        if media is None:
            raise MediaDoesNotExist(f"Media with id {id!r} does not exist")
        self._repository.delete(id)
        await self._event_bus.publish([MediaDeletedDomainEvent.create({"id": id})])
