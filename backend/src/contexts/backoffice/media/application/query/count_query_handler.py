from src.contexts.backoffice.media.domain import MediaRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .count_query import MediaCountQuery


class MediaCountQueryHandler(QueryHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return MediaCountQuery

    async def handle(self, query: MediaCountQuery) -> int:
        return self.repository.count()
