import datetime
import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import MediaRepository
from src.contexts.shared.domain import NotFound
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.infrastructure.file_manager import FileManager

from .update_command import MediaUpdateCommand


class MediaUpdateCommandHandler:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager("var/storage/media/")

    def subscribed_to(self) -> Command:
        return MediaUpdateCommand

    def handle(self, command: MediaUpdateCommand) -> None:
        media = self._repository.search(command.id)
        if media is None:
            raise NotFound(f"Media: {command.id!r} not found")
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media.update(command.title, size, duration, file_path)
        self._repository.save(media)
