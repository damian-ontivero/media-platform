from fastapi import Response, status
from src.apps.backoffice.api.v0.schemas import SerieWriteSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.series.application.command.create_command_handler import SerieCreateCommand
from src.contexts.shared.domain.bus.command import CommandBus


class SeriePostController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, serie: SerieWriteSchema) -> Response:
        self._command_bus.dispatch(SerieCreateCommand(**serie.model_dump()))
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type=None)
