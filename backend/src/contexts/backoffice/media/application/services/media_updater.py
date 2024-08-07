from src.contexts.backoffice.media.domain.media_exceptions import MediaAlreadyExists
from src.contexts.backoffice.media.domain.media_exceptions import MediaDoesNotExist
from src.contexts.backoffice.media.domain.media_repository import MediaRepository
from src.contexts.shared.domain.criteria.criteria import Criteria
from src.contexts.shared.domain.event_bus.event_bus import EventBus


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
