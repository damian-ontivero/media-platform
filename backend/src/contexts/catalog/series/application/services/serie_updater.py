from src.contexts.catalog.series.domain.serie_repository import SerieRepository
from src.contexts.catalog.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from src.contexts.shared.domain.event_bus.event_bus import EventBus
from src.contexts.shared.domain.query_bus.query_bus import QueryBus


class SerieUpdater:
    def __init__(self, repository: SerieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, id: str, title: str, seasons: list) -> None:
        await self._ensure_media_is_available(seasons)
        serie = self._repository.search(id)
        serie.update(title, seasons)
        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_domain_events())

    async def _ensure_media_is_available(self, seasons: list) -> None:
        for season in seasons:
            for episode in season["episodes"]:
                episode["duration"] = await self._query_bus.ask(MediaFindByIdQuery(episode["media_id"]))
                del episode["media_id"]
