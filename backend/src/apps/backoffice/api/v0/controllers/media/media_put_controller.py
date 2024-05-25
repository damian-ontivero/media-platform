from fastapi import Response, UploadFile, status
from src.contexts.backoffice.media.application.media_updater import MediaUpdater

from ...schemas import MediaWriteSchema
from ..controller import Controller


class MediaPutController(Controller):
    def __init__(self, updater: MediaUpdater) -> None:
        self._updater = updater

    async def run(self, id: str, media: MediaWriteSchema, file: UploadFile) -> Response:
        self._updater.run(id=id, **media.model_dump(), file_name=file.filename, file=await file.read())
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
