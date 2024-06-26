from src.contexts.catalog.movies.domain import Movie, MovieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.criteria import Criteria

from .search_by_criteria_query import MovieSearchByCriteriaQuery


class MovieSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return MovieSearchByCriteriaQuery

    def handle(self, query: MovieSearchByCriteriaQuery) -> list[Movie]:
        criteria = Criteria.from_primitives(query.filter, query.sort, query.page_size, query.page_number)
        return self.repository.matching(criteria)
