from fastapi import Request, Response, status

from src.contexts.channel.content.application.content_updater import (
    ContentUpdater,
)

from .controller import Controller


class ContentPutController(Controller):

    def __init__(self, updater: ContentUpdater) -> None:
        self._updater = updater

    async def run(self, request: Request) -> Response:
        data = await request.json()
        self._updater.run(
            id=request.path_params["id"],
            files=data["files"],
            rating=data["rating"],
            metadata_=data["metadata_"],
            channel_id=data["channel_id"],
        )
        return Response(
            content=None,
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
