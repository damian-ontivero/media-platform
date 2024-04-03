from fastapi import Request, Response, status

from src.contexts.channel.channel.application.channel_searcher import (
    ChannelSearcher,
)

from ..schemas.channel import ChannelPaginatedResponseSchema
from .controller import Controller


class ChannelsGetController(Controller):

    def __init__(self, searcher: ChannelSearcher) -> None:
        self._searcher = searcher

    def run(self, request: Request) -> Response:
        channels = self._searcher.run()
        response = ChannelPaginatedResponseSchema(
            items=[channel.to_primitives() for channel in channels],
        )
        return Response(
            content=response.model_dump_json(),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
