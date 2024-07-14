from src.contexts.backoffice.movies.application.services import MovieCounter
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .movie_count_query import MovieCountQuery


class MovieCountQueryHandler(QueryHandler):
    def __init__(self, counter: MovieCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> Query:
        return MovieCountQuery

    async def handle(self, query: MovieCountQuery) -> int:
        return self._counter.run()
