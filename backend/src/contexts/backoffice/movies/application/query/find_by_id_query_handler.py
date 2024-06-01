from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain import EntityNotFound
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import MovieFindByIdQuery


class MovieFindByIdQueryHandler(QueryHandler):
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return MovieFindByIdQuery

    def handle(self, query: MovieFindByIdQuery) -> Movie:
        movie = self.repository.search(query.id)
        if movie is None:
            raise EntityNotFound(f"Movie: {query.id!r} not found")
        return movie
