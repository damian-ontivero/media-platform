from src.contexts.catalog.media.domain import Media, MediaRepository
from src.contexts.shared.domain.bus.event import EventBus


class MediaCreator:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, title: str, size: int, duration: int, path: str) -> None:
        media = Media.create(title, size, duration, path)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())
