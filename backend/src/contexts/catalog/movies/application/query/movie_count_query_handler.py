from src.contexts.catalog.movies.domain import MovieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .movie_count_query import MovieCountQuery


class MovieCountQueryHandler(QueryHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Query:
        return MovieCountQuery

    async def handle(self, query: MovieCountQuery) -> int:
        return self._repository.count()
