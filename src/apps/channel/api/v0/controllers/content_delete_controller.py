from fastapi import Request, Response, status

from src.contexts.channel.content.application.content_eliminator import (
    ContentEliminator,
)

from .controller import Controller


class ContentDeleteController(Controller):

    def __init__(self, eliminator: ContentEliminator) -> None:
        self._eliminator = eliminator

    async def run(self, request: Request) -> Response:
        self._eliminator.run(request.path_params["id"])
        return Response(
            content=None,
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
