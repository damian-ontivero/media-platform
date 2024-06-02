from fastapi import Response, status
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.series.application.command.delete_command import SerieDeleteCommand
from src.contexts.shared.domain.bus.command import CommandBus


class SerieDeleteController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str) -> Response:
        self._command_bus.dispatch(SerieDeleteCommand(id))
        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
