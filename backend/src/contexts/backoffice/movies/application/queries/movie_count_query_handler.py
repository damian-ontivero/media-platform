from src.contexts.backoffice.movies.application.queries.movie_count_query import MovieCountQuery
from src.contexts.backoffice.movies.application.services.movie_counter import MovieCounter
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class MovieCountQueryHandler(QueryHandler):
    def __init__(self, counter: MovieCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> Query:
        return MovieCountQuery

    async def handle(self, query: MovieCountQuery) -> int:
        return self._counter.run()
