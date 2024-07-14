from src.contexts.backoffice.media.application.services import MediaCounter
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .media_count_query import MediaCountQuery


class MediaCountQueryHandler(QueryHandler):
    def __init__(self, counter: MediaCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> Query:
        return MediaCountQuery

    async def handle(self, query: MediaCountQuery) -> int:
        return self._counter.run()
