import os

from moviepy.editor import VideoFileClip

from src.contexts.backoffice.media.application.commands.media_create_command import MediaCreateCommand
from src.contexts.backoffice.media.application.services.media_creator import MediaCreator
from src.contexts.shared.domain.command_bus.command import Command
from src.contexts.shared.domain.command_bus.command_handler import CommandHandler
from src.contexts.shared.infrastructure.file_manager.file_manager import FileManager

MEDIA_STORAGE_PATH = os.getenv("MEDIA_STORAGE_PATH")


class MediaCreateCommandHandler(CommandHandler):
    def __init__(self, creator: MediaCreator) -> None:
        self._creator = creator
        self._file_manager = FileManager(MEDIA_STORAGE_PATH)

    @staticmethod
    def subscribed_to() -> Command:
        return MediaCreateCommand

    async def handle(self, command: MediaCreateCommand) -> None:
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        await self._creator.run(command.title, size, duration, file_path)
