from src.contexts.backoffice.series.domain import Serie, SerieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.criteria import Criteria

from .search_by_criteria_query import SerieSearchByCriteriaQuery


class SerieSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return SerieSearchByCriteriaQuery

    async def handle(self, query: SerieSearchByCriteriaQuery) -> list[Serie]:
        criteria = Criteria.from_primitives(query.filter, query.sort, query.page_size, query.page_number)
        return self.repository.matching(criteria)
