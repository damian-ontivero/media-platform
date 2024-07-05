import os

from moviepy.editor import VideoFileClip
from src.contexts.backoffice.media.domain import Media, MediaAlreadyExists, MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.domain.criteria import Criteria
from src.contexts.shared.infrastructure.file_manager import FileManager

from .media_create_command import MediaCreateCommand

MEDIA_STORAGE_PATH = os.getenv("MEDIA_STORAGE_PATH")


class MediaCreateCommandHandler(CommandHandler):
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus
        self._file_manager = FileManager(MEDIA_STORAGE_PATH)

    def subscribed_to(self) -> Command:
        return MediaCreateCommand

    async def handle(self, command: MediaCreateCommand) -> None:
        self._ensure_title_is_available(command)
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration
        media = Media.create(command.title, size, duration, file_path)
        self._repository.save(media)
        await self._event_bus.publish(media.pull_domain_events())

    def _ensure_title_is_available(self, command: MediaCreateCommand) -> None:
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
