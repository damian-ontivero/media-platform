from src.contexts.backoffice.series.application.services import SerieCounter
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .serie_count_query import SerieCountQuery


class SerieCountQueryHandler(QueryHandler):
    def __init__(self, counter: SerieCounter) -> None:
        self._counter = counter

    def subscribed_to(self) -> Query:
        return SerieCountQuery

    async def handle(self, query: SerieCountQuery) -> int:
        return self._counter.run()
