from fastapi import Response, UploadFile, status
from src.contexts.backoffice.media.application.media_creator import MediaCreator

from ...schemas import MediaWriteSchema
from ..controller import Controller


class MediaPostController(Controller):
    def __init__(self, creator: MediaCreator) -> None:
        self._creator = creator

    async def run(self, media: MediaWriteSchema, file: UploadFile) -> Response:
        self._creator.run(**media.model_dump(), file_name=file.filename, file=await file.read())
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type="application/json")
