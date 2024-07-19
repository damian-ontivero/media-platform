from src.contexts.backoffice.series.domain.serie_events import SerieDeletedDomainEvent
from src.contexts.backoffice.series.domain.serie_exceptions import SerieDoesNotExist
from src.contexts.backoffice.series.domain.serie_repository import SerieRepository
from src.contexts.shared.domain.event_bus.event_bus import EventBus


class SerieDeleter:
    def __init__(self, repository: SerieRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str) -> None:
        serie = self._repository.search(id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {id!r} does not exist")
        self._repository.delete(id)
        await self._event_bus.publish([SerieDeletedDomainEvent.create({"id": id})])
