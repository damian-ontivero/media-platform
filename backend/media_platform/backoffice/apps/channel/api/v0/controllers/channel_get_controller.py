from fastapi import Request, Response, status
from media_platform.backoffice.contexts.channel.channel.application.channel_finder import (
    ChannelFinder,
)

from ..schemas import ChannelGetSchema
from .controller import Controller


class ChannelGetController(Controller):

    def __init__(self, finder: ChannelFinder) -> None:
        self._finder = finder

    def run(self, request: Request) -> Response:
        channel = self._finder.run(request.path_params["id"])
        response = ChannelGetSchema(**channel.to_primitives())
        return Response(
            content=response.model_dump_json(),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
