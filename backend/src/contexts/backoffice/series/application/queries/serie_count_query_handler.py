from src.contexts.backoffice.series.application.queries.serie_count_query import SerieCountQuery
from src.contexts.backoffice.series.application.services.serie_counter import SerieCounter
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class SerieCountQueryHandler(QueryHandler):
    def __init__(self, counter: SerieCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> Query:
        return SerieCountQuery

    async def handle(self, query: SerieCountQuery) -> int:
        return self._counter.run()
