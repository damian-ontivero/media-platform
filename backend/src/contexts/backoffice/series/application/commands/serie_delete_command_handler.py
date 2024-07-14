from src.contexts.backoffice.series.application.services import SerieDeleter
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .serie_delete_command import SerieDeleteCommand


class SerieDeleteCommandHandler(CommandHandler):
    def __init__(self, deleter: SerieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> Command:
        return SerieDeleteCommand

    async def handle(self, command: SerieDeleteCommand) -> None:
        await self._deleter.run(command.id)
