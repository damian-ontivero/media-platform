from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain import NotFound


class MovieUpdater:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, id: str, title: str, media_id: str) -> None:
        movie = self._repository.search(id)
        if movie is None:
            raise NotFound(f"Movie: {id!r} not found")
        movie.update(title, media_id)
        self._repository.save(movie)
