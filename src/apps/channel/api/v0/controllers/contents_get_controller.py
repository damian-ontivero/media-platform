import base64
import json

from fastapi import Request, Response, status

from src.contexts.channel.content.application.content_searcher import (
    ContentSearcher,
)

from ..schemas.content import ContentPaginatedResponseSchema
from .controller import Controller


class ContentsGetController(Controller):

    def __init__(self, searcher: ContentSearcher) -> None:
        self._searcher = searcher

    def run(self, request: Request) -> Response:
        criteria = {
            "filter": {},
            "sort": [],
            "page_size": 15,
            "page_number": 1,
        }
        request_criteria = request.query_params.get("criteria")
        if request_criteria is not None:
            criteria = json.loads(base64.b64decode(request_criteria).decode())
        contents = self._searcher.run(criteria)
        response = ContentPaginatedResponseSchema(
            items=[content.to_primitives() for content in contents],
        )
        return Response(
            content=response.model_dump_json(),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )
