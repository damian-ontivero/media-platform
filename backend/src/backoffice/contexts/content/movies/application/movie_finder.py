from src.backoffice.contexts.content.movies.domain.movie import Movie
from src.backoffice.contexts.content.movies.domain.movie_repository import MovieRepository


class MovieFinder:
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    def run(self, id: str) -> Movie:
        movie = self.repository.search(id)
        if movie is None:
            raise ValueError(f"Movie: {id!r} not found")
        return movie
