from src.backoffice.contexts.content.movies.domain.movie_repository import MovieRepository


class MovieEliminator:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> None:
        movie = self._repository.search(id)
        if movie is None:
            raise Exception(f"Movie: {id!r} not found")
        self._repository.delete(id)
