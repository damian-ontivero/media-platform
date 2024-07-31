from src.contexts.backoffice.media.application.queries.media_count_query import MediaCountQuery
from src.contexts.backoffice.media.application.services.media_counter import MediaCounter
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class MediaCountQueryHandler(QueryHandler):
    def __init__(self, counter: MediaCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> Query:
        return MediaCountQuery

    async def handle(self, query: MediaCountQuery) -> int:
        return self._counter.run()
