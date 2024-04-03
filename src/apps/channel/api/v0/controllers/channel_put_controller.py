from fastapi import Request, Response, status

from src.contexts.channel.channel.application.channel_updater import (
    ChannelUpdater,
)

from .controller import Controller


class ChannelPutController(Controller):

    def __init__(self, updater: ChannelUpdater) -> None:
        self._updater = updater

    async def run(self, request: Request) -> Response:
        data = await request.json()
        self._updater.run(
            id=request.path_params["id"],
            title=data["title"],
            languages=data["languages"],
            picture=data["picture"],
        )
        return Response(
            content=None,
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
