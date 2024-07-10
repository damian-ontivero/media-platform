from src.contexts.backoffice.media.domain import MediaAlreadyExists, MediaDoesNotExist, MediaRepository
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.criteria import Criteria


class MediaUpdater:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str, title: str, size: int, duration: int, path: str) -> None:
        media = self._repository.search(id)
        if media is None:
            raise MediaDoesNotExist(f"Media with id {id!r} does not exist")
        self._ensure_title_is_available(id, title)
        media.update(title, size, duration, path)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())

    def _ensure_title_is_available(self, id: str, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={
                "conjunction": "AND",
                "conditions": [
                    {"field": "id", "operator": "NOT_EQUALS", "value": id},
                    {"field": "title", "operator": "EQUALS", "value": title},
                ],
            },
            sort=None,
            page_size=None,
            page_number=None,
        )
        exists = self._repository.matching(criteria)
        if exists:
            raise MediaAlreadyExists("A media with the same title already exists")
