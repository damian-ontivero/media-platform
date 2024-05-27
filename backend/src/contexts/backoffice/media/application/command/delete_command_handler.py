from src.contexts.backoffice.media.domain import MediaRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .delete_command import MediaDeleteCommand


class MediaDeleteCommandHandler(CommandHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Command:
        return MediaDeleteCommand

    def handle(self, command: MediaDeleteCommand) -> None:
        media = self._repository.search(command.id)
        if media is None:
            raise Exception(f"Media: {command.id!r} not found")
        self._repository.delete(command.id)
