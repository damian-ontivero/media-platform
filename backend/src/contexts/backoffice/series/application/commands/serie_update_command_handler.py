from src.contexts.backoffice.series.application.commands.serie_update_command import SerieUpdateCommand
from src.contexts.backoffice.series.application.services.serie_updater import SerieUpdater
from src.contexts.shared.domain.command_bus.command import Command
from src.contexts.shared.domain.command_bus.command_handler import CommandHandler


class SerieUpdateCommandHandler(CommandHandler):
    def __init__(self, updater: SerieUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> Command:
        return SerieUpdateCommand

    async def handle(self, command: SerieUpdateCommand) -> None:
        await self._updater.run(command.id, command.title, command.seasons)
