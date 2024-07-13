from src.contexts.catalog.movies.domain import MovieDeletedDomainEvent, MovieRepository
from src.contexts.shared.domain.bus.event import EventBus


class MovieDeleter:
    def __init__(self, repository: MovieRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str) -> None:
        self._repository.delete(id)
        await self._event_bus.publish([MovieDeletedDomainEvent.create({"id": id})])
