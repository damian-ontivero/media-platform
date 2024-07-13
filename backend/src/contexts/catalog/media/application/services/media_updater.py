from src.contexts.catalog.media.domain import MediaRepository
from src.contexts.shared.domain.bus.event import EventBus


class MediaUpdater:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str, title: str, size: int, duration: int, path: str) -> None:
        media = self._repository.search(id)
        media.update(title, size, duration, path)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())
