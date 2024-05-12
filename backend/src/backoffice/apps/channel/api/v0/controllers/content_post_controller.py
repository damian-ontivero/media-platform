import json

from fastapi import Request, Response, status
from src.backoffice.contexts.channel.content.application.content_creator import ContentCreator

from .controller import Controller


class ContentPostController(Controller):
    def __init__(self, creator: ContentCreator) -> None:
        self._creator = creator

    async def run(self, request: Request) -> Response:
        data = await request.form()
        files = []
        for file in data.getlist("files"):
            files.append({"name": file.filename, "data": file.file.read(), "media_type": file.content_type})
        self._creator.run(
            rating=data["rating"], metadata_=json.loads(data["metadata_"]), channel_id=data["channel_id"], files=files
        )
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type="application/json")
