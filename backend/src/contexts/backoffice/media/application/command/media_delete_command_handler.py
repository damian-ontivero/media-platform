from src.contexts.backoffice.media.domain import MediaDeletedDomainEvent, MediaDoesNotExist, MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event import EventBus

from .media_delete_command import MediaDeleteCommand


class MediaDeleteCommandHandler(CommandHandler):
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return MediaDeleteCommand

    async def handle(self, command: MediaDeleteCommand) -> None:
        media = self._repository.search(command.id)
        if media is None:
            raise MediaDoesNotExist(f"Media with id {command.id!r} does not exist")
        self._repository.delete(command.id)
        await self._event_bus.publish([MediaDeletedDomainEvent.create({"id": command.id})])
