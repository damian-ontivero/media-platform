from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository


class MovieCreator:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, title: str, media_id: str) -> None:
        movie = Movie.create(title, media_id)
        self._repository.save(movie)
