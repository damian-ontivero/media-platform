from fastapi import Response, status
from src.contexts.backoffice.movies.application.command.create_command_handler import MovieCreateCommand
from src.contexts.shared.domain.bus.command import CommandBus

from ...schemas import MovieWriteSchema
from ..controller import Controller


class MoviePostController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, movie: MovieWriteSchema) -> Response:
        self._command_bus.dispatch(MovieCreateCommand(**movie.model_json_schema()))
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type=None)
