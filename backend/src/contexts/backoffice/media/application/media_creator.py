import os

from dotenv import load_dotenv
from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.infrastructure.file_manager import FileManager

load_dotenv()


CONTENT_STORAGE_PATH = os.getenv("CONTENT_STORAGE_PATH")


class MediaCreator:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager("var/storage/media/")

    def run(self, title: str, file_name: str, file: bytes) -> None:
        file_path = self._file_manager.save_file(title, file_name, file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media = Media.create(title, size, duration, file_path)
        self._repository.save(media)
