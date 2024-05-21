import base64
import json

from fastapi import Response, status
from src.contexts.backoffice.media.application.media_searcher import MediaSearcher

from ...schemas import MediaPaginatedResponseSchema
from ..controller import Controller


class MediasGetController(Controller):
    def __init__(self, searcher: MediaSearcher) -> None:
        self._searcher = searcher

    def run(self, criteria: str | None) -> Response:
        if criteria is not None:
            criteria = json.loads(base64.b64decode(criteria).decode())
        medias = self._searcher.run(criteria)
        response = MediaPaginatedResponseSchema(items=[media.to_primitives() for media in medias])
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
