import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.application.services import MediaUpdater
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.infrastructure.file_manager import FileManager

from .media_update_command import MediaUpdateCommand

MEDIA_STORAGE_PATH = os.getenv("MEDIA_STORAGE_PATH")


class MediaUpdateCommandHandler(CommandHandler):
    def __init__(self, updater: MediaUpdater) -> None:
        self._updater = updater
        self._file_manager = FileManager(MEDIA_STORAGE_PATH)

    @staticmethod
    def subscribed_to() -> Command:
        return MediaUpdateCommand

    async def handle(self, command: MediaUpdateCommand) -> None:
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        await self._updater.run(command.id, command.title, size, duration, file_path)
