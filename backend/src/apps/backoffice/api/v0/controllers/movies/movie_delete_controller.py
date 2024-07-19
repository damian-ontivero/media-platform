from fastapi import Response, status
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.movies.application.commands.movie_delete_command import MovieDeleteCommand
from src.contexts.shared.domain.command_bus.command_bus import CommandBus


class MovieDeleteController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str) -> Response:
        await self._command_bus.dispatch(MovieDeleteCommand(id))
        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
