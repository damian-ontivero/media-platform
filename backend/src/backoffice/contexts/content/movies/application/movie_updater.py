from src.backoffice.contexts.content.movies.domain.movie_repository import MovieRepository


class MovieUpdater:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, id: str, files: list[dict], rating: float, metadata_: dict, channel_id: str) -> None:
        movie = self._repository.search(id)
        if movie is None:
            raise Exception(f"Movie: {id!r} not found")
        movie.update(files, rating, metadata_, channel_id)
        self._repository.save(movie)
