from src.contexts.catalog.movies.domain import Movie, MovieDoesNotExist, MovieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .movie_find_by_id_query import MovieFindByIdQuery


class MovieFindByIdQueryHandler(QueryHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Query:
        return MovieFindByIdQuery

    async def handle(self, query: MovieFindByIdQuery) -> Movie:
        movie = self._repository.search(query.id)
        if movie is None:
            raise MovieDoesNotExist(f"Movie with id {query.id!r} does not exist")
        return movie
