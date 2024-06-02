from fastapi import Response, status
from src.apps.backoffice.api.v0.schemas import SerieWriteSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.series.application.command.update_command import SerieUpdateCommand
from src.contexts.shared.domain.bus.command import CommandBus


class SeriePutController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str, serie: SerieWriteSchema) -> Response:
        self._command_bus.dispatch(SerieUpdateCommand(id, **serie.model_dump()))
        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
