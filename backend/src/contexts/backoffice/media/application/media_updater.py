import datetime
import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import MediaRepository
from src.contexts.shared.domain import NotFound
from src.contexts.shared.infrastructure.file_manager import FileManager


class MediaUpdater:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager("var/storage/media/")

    def run(self, id: str, title: str, file_name: str, file: bytes) -> None:
        media = self._repository.search(id)
        if media is None:
            raise NotFound(f"Media: {id!r} not found")
        file_path = self._file_manager.save_file(title, file_name, file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media.update(title, size, duration, file_path)
        self._repository.save(media)
