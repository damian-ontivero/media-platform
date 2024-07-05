from src.contexts.catalog.media.domain import MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus

from .media_update_command import MediaUpdateCommand


class MediaUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return MediaUpdateCommand

    async def handle(self, command: MediaUpdateCommand) -> None:
        media = self._repository.search(command.id)
        if media is not None:
            media.update(command.title, command.size, command.duration, command.file_path)
            self._repository.save(media)
            await self._event_bus.publish(media.pull_domain_events())
