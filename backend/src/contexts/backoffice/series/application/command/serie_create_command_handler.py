from src.contexts.backoffice.series.application.services import SerieCreator
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .serie_create_command import SerieCreateCommand


class SerieCreateCommandHandler(CommandHandler):
    def __init__(self, creator: SerieCreator) -> None:
        self._creator = creator

    def subscribed_to(self) -> Command:
        return SerieCreateCommand

    async def handle(self, command: SerieCreateCommand) -> None:
        await self._creator.run(command.title, command.seasons)
