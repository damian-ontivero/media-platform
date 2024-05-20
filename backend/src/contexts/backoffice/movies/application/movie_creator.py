import os

from dotenv import load_dotenv
from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.infrastructure.file_manager import FileManager

load_dotenv()


CONTENT_STORAGE_PATH = os.getenv("CONTENT_STORAGE_PATH")


class MovieCreator:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager("var/storage/movie/")

    def run(self, files: dict, rating: float, metadata_: dict, channel_id: str) -> None:
        movie_files = []
        for file in files:
            path = self._file_manager.save_file(CONTENT_STORAGE_PATH, file.get("name"), file.get("data"))
            movie_files.append({"name": file.get("name"), "path": path, "media_type": file.get("media_type")})
        movie = Movie.create(movie_files, rating, metadata_, channel_id)
        self._repository.save(movie)
