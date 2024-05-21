from fastapi import Response, status
from src.contexts.backoffice.media.application.media_updater import MediaUpdater

from ...schemas import MediaUpdateSchema
from ..controller import Controller


class MediaPutController(Controller):
    def __init__(self, updater: MediaUpdater) -> None:
        self._updater = updater

    async def run(self, id: str, media: MediaUpdateSchema) -> Response:
        self._updater.run(id=id, **media.model_json_schema())
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
