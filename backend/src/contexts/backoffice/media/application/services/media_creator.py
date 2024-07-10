from src.contexts.backoffice.media.domain import Media, MediaAlreadyExists, MediaRepository
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.criteria import Criteria


class MediaCreator:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, title: str, size: int, duration: int, path: str) -> None:
        self._ensure_title_is_available(title)
        media = Media.create(title, size, duration, path)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())

    def _ensure_title_is_available(self, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": title}]},
            sort=None,
            page_size=None,
            page_number=None,
        )
        title = self._repository.matching(criteria)
        if title:
            raise MediaAlreadyExists("A media with the same title already exists")
