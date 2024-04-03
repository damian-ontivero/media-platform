from fastapi import Request, Response, status

from src.contexts.channel.channel.application.channel_finder import (
    ChannelFinder,
)
from src.contexts.channel.content.application.content_searcher import (
    ContentSearcher,
)

from ..schemas import ChannelGetSchema
from .controller import Controller


class ChannelRatingGetController(Controller):

    def __init__(
        self, channel_finder: ChannelFinder, content_searcher: ContentSearcher
    ) -> None:
        self._channel_finder = channel_finder
        self._content_searcher = content_searcher

    def run(self, request: Request) -> Response:
        channel = self._channel_finder.run(request.path_params["id"])
        criteria = {
            "filter": {
                "conjunction": "AND",
                "conditions": [
                    {
                        "field": "channel_id",
                        "operator": "EQUALS",
                        "value": channel.id.value,
                    },
                ],
            },
            "sort": [],
            "page_size": 15,
            "page_number": 1,
        }
        content = self._content_searcher.run(criteria)
        rating_sum = sum([content.rating for content in content])
        rating_avg = rating_sum / len(content) if len(content) > 0 else 0
        return Response(
            content=str(round(rating_avg, 2)),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
