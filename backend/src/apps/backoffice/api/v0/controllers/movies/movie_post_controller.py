from fastapi import Response, status
from src.apps.backoffice.api.v0.schemas import MovieWriteSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.movies.application.command.create_command_handler import MovieCreateCommand
from src.contexts.shared.domain.bus.command import CommandBus


class MoviePostController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, movie: MovieWriteSchema) -> Response:
        await self._command_bus.dispatch(MovieCreateCommand(**movie.model_dump()))
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type=None)
