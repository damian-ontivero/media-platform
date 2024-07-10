from src.contexts.backoffice.movies.application.services import MovieFinder
from src.contexts.backoffice.movies.domain import Movie
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .movie_find_by_id_query import MovieFindByIdQuery


class MovieFindByIdQueryHandler(QueryHandler):
    def __init__(self, finder: MovieFinder) -> None:
        self._finder = finder

    def subscribed_to(self) -> Query:
        return MovieFindByIdQuery

    async def handle(self, query: MovieFindByIdQuery) -> Movie:
        return self._finder.run(query.id)
