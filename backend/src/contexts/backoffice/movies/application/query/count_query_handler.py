from src.contexts.backoffice.movies.domain import MovieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .count_query import MovieCountQuery


class MovieCountQueryHandler(QueryHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return MovieCountQuery

    def handle(self, query: MovieCountQuery) -> int:
        return self.repository.count()
