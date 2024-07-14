from src.contexts.backoffice.media.application.services import MediaDeleter
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .media_delete_command import MediaDeleteCommand


class MediaDeleteCommandHandler(CommandHandler):
    def __init__(self, deleter: MediaDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> Command:
        return MediaDeleteCommand

    async def handle(self, command: MediaDeleteCommand) -> None:
        await self._deleter.run(command.id)
