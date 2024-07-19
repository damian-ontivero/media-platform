from src.contexts.backoffice.movies.application.queries.movie_find_by_id_query import MovieFindByIdQuery
from src.contexts.backoffice.movies.application.services.movie_finder import MovieFinder
from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class MovieFindByIdQueryHandler(QueryHandler):
    def __init__(self, finder: MovieFinder) -> None:
        self._finder = finder

    @staticmethod
    def subscribed_to() -> Query:
        return MovieFindByIdQuery

    async def handle(self, query: MovieFindByIdQuery) -> Movie:
        return self._finder.run(query.id)
