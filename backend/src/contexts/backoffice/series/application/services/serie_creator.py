from src.contexts.backoffice.series.domain import Serie, SerieAlreadyExists, SerieRepository
from src.contexts.backoffice.shared.media.application.queries import MediaFindByIdQuery
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.bus.query import QueryBus
from src.contexts.shared.domain.criteria import Criteria


class SerieCreator:
    def __init__(self, repository: SerieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, title: str, seasons: list) -> None:
        self._ensure_title_is_available(title)
        await self._ensure_media_is_available(seasons)
        serie = Serie.create(title, seasons)
        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_domain_events())

    def _ensure_title_is_available(self, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": title}]},
            sort=None,
            page_size=None,
            page_number=None,
        )
        title = self._repository.matching(criteria)
        if title:
            raise SerieAlreadyExists("A serie with the same title already exists")

    async def _ensure_media_is_available(self, seasons: list) -> None:
        for season in seasons:
            for episode in season["episodes"]:
                await self._query_bus.ask(MediaFindByIdQuery(episode["media_id"]))
