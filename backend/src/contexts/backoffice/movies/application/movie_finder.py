from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain import NotFound


class MovieFinder:
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    def run(self, id: str) -> Movie:
        movie = self.repository.search(id)
        if movie is None:
            raise NotFound(f"Movie: {id!r} not found")
        return movie
