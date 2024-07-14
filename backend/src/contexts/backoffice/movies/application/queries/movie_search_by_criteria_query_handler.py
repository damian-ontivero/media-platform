from src.contexts.backoffice.movies.application.services import MovieSearcher
from src.contexts.backoffice.movies.domain import Movie
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .movie_search_by_criteria_query import MovieSearchByCriteriaQuery


class MovieSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, searcher: MovieSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> Query:
        return MovieSearchByCriteriaQuery

    async def handle(self, query: MovieSearchByCriteriaQuery) -> list[Movie]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
