from src.contexts.catalog.media.domain import MediaRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .media_count_query import MediaCountQuery


class MediaCountQueryHandler(QueryHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Query:
        return MediaCountQuery

    async def handle(self, query: MediaCountQuery) -> int:
        return self._repository.count()
