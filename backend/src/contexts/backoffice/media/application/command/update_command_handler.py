import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import MediaAlreadyExists, MediaDoesNotExist, MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.criteria.criteria import Criteria
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
        self._ensure_title_is_available(command)
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media.update(command.title, size, duration, file_path)
        self._repository.save(media)

    def _ensure_title_is_available(self, command: MediaUpdateCommand) -> None:
        criteria = Criteria.from_primitives(
            filter={
                "conjunction": "AND",
                "conditions": [{"field": "title", "operator": "EQUALS", "value": command.title}],
            },
            sort=None,
            page_size=None,
            page_number=None,
        )
        media = self._repository.matching(criteria)
        if media:
            raise MediaAlreadyExists("A media with the same title already exists")
