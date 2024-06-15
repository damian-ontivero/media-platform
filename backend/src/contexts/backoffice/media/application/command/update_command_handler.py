import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import MediaDoesNotExist, MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.infrastructure.file_manager import FileManager

from .update_command import MediaUpdateCommand

MEDIA_STORAGE_PATH = os.getenv("MEDIA_STORAGE_PATH")


class MediaUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager(MEDIA_STORAGE_PATH)

    def subscribed_to(self) -> Command:
        return MediaUpdateCommand

    def handle(self, command: MediaUpdateCommand) -> None:
        media = self._repository.search(command.id)
        if media is None:
            raise MediaDoesNotExist(f"Media with id {command.id!r} does not exist")
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media.update(command.title, size, duration, file_path)
        self._repository.save(media)
