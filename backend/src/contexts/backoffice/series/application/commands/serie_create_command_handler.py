from src.contexts.backoffice.series.application.commands.serie_create_command import SerieCreateCommand
from src.contexts.backoffice.series.application.services.serie_creator import SerieCreator
from src.contexts.shared.domain.command_bus.command import Command
from src.contexts.shared.domain.command_bus.command_handler import CommandHandler


class SerieCreateCommandHandler(CommandHandler):
    def __init__(self, creator: SerieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> Command:
        return SerieCreateCommand

    async def handle(self, command: SerieCreateCommand) -> None:
        await self._creator.run(command.title, command.seasons)
