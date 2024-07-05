from src.contexts.backoffice.series.domain import SerieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .serie_count_query import SerieCountQuery


class SerieCountQueryHandler(QueryHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Query:
        return SerieCountQuery

    async def handle(self, query: SerieCountQuery) -> int:
        return self._repository.count()
