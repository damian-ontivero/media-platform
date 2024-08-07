from src.contexts.backoffice.series.domain.serie_exceptions import SerieAlreadyExists
from src.contexts.backoffice.series.domain.serie_exceptions import SerieDoesNotExist
from src.contexts.backoffice.series.domain.serie_repository import SerieRepository
from src.contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from src.contexts.shared.domain.criteria.criteria import Criteria
from src.contexts.shared.domain.event_bus.event_bus import EventBus
from src.contexts.shared.domain.query_bus.query_bus import QueryBus


class SerieUpdater:
    def __init__(self, repository: SerieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, id: str, title: str, seasons: list) -> None:
        serie = self._repository.search(id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {id!r} does not exist")
        self._ensure_title_is_available(id, title)
        await self._ensure_media_is_available(seasons)
        serie.update(title, seasons)
        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_domain_events())

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
            raise SerieAlreadyExists("A serie with the same title already exists")

    async def _ensure_media_is_available(self, seasons: list) -> None:
        for season in seasons:
            for episode in season["episodes"]:
                await self._query_bus.ask(MediaFindByIdQuery(episode["media_id"]))
