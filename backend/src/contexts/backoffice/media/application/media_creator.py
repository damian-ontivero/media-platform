import os

from dotenv import load_dotenv
from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.infrastructure.file_manager import FileManager

load_dotenv()


CONTENT_STORAGE_PATH = os.getenv("CONTENT_STORAGE_PATH")


class MediaCreator:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager("var/storage/media/")

    def run(self, files: dict, rating: float, metadata_: dict, channel_id: str) -> None:
        media_files = []
        for file in files:
            path = self._file_manager.save_file(CONTENT_STORAGE_PATH, file.get("name"), file.get("data"))
            media_files.append({"name": file.get("name"), "path": path, "media_type": file.get("media_type")})
        media = Media.create(media_files, rating, metadata_, channel_id)
        self._repository.save(media)
