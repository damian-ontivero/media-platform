from src.contexts.backoffice.series.application.services import SerieUpdater
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .serie_update_command import SerieUpdateCommand


class SerieUpdateCommandHandler(CommandHandler):
    def __init__(self, updater: SerieUpdater) -> None:
        self._updater = updater

    def subscribed_to(self) -> Command:
        return SerieUpdateCommand

    async def handle(self, command: SerieUpdateCommand) -> None:
        await self._updater.run(command.id, command.title, command.seasons)
