from src.contexts.backoffice.series.application.services import SerieSearcher
from src.contexts.backoffice.series.domain import Serie
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .serie_search_by_criteria_query import SerieSearchByCriteriaQuery


class SerieSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, searcher: SerieSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> Query:
        return SerieSearchByCriteriaQuery

    async def handle(self, query: SerieSearchByCriteriaQuery) -> list[Serie]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
