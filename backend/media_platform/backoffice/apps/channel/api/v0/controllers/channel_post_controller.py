from fastapi import Request, Response, status
from media_platform.backoffice.contexts.channel.channel.application.channel_creator import (
    ChannelCreator,
)

from .controller import Controller


class ChannelPostController(Controller):

    def __init__(self, creator: ChannelCreator) -> None:
        self._creator = creator

    async def run(self, request: Request) -> Response:
        data = await request.json()
        self._creator.run(
            title=data["title"],
            languages=data["languages"],
            image=data["image"],
        )
        return Response(
            content=None,
            status_code=status.HTTP_201_CREATED,
            media_type="application/json",
        )
