from src.contexts.backoffice.movies.application.queries.movie_search_by_criteria_query import MovieSearchByCriteriaQuery
from src.contexts.backoffice.movies.application.services.movie_searcher import MovieSearcher
from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class MovieSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, searcher: MovieSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> Query:
        return MovieSearchByCriteriaQuery

    async def handle(self, query: MovieSearchByCriteriaQuery) -> list[Movie]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
