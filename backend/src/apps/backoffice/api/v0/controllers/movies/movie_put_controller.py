from fastapi import Response, status
from src.contexts.backoffice.movies.application.command.update_command import MovieUpdateCommand
from src.contexts.shared.domain.bus.command import CommandBus

from ...schemas import MovieWriteSchema
from ..controller import Controller


class MoviePutController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str, movie: MovieWriteSchema) -> Response:
        self._command_bus.dispatch(MovieUpdateCommand(id, **movie.model_json_schema()))
        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
