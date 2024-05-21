from fastapi import Response, status
from src.contexts.backoffice.media.application.media_eliminator import MediaEliminator

from ..controller import Controller


class MediaDeleteController(Controller):
    def __init__(self, eliminator: MediaEliminator) -> None:
        self._eliminator = eliminator

    async def run(self, id: str) -> Response:
        self._eliminator.run(id)
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
