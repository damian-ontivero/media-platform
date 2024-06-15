import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.infrastructure.file_manager import FileManager

from .create_command import MediaCreateCommand

MEDIA_STORAGE_PATH = os.getenv("MEDIA_STORAGE_PATH")


class MediaCreateCommandHandler(CommandHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager(MEDIA_STORAGE_PATH)

    def subscribed_to(self) -> Command:
        return MediaCreateCommand

    def handle(self, command: MediaCreateCommand) -> None:
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media = Media.create(command.title, size, duration, file_path)
        self._repository.save(media)
