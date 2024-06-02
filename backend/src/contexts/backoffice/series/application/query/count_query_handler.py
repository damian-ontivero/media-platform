from src.contexts.backoffice.series.domain import SerieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .count_query import SerieCountQuery


class SerieCountQueryHandler(QueryHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return SerieCountQuery

    def handle(self, query: SerieCountQuery) -> int:
        return self.repository.count()