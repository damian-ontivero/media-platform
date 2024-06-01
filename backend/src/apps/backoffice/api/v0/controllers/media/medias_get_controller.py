import base64
import json

from fastapi import Response, status
from src.apps.backoffice.api.v0.schemas import MediaPaginatedResponseSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.media.application.query import MediaSearchByCriteriaQuery
from src.contexts.shared.domain.bus.query import QueryBus


class MediasGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    def run(self, criteria: str | None) -> Response:
        if criteria is None:
            criteria = {"filter": {}, "sort": [], "page_size": 10, "page_number": 1}
            criteria = base64.b64encode(json.dumps(criteria).encode()).decode()
        criteria = json.loads(base64.b64decode(criteria).decode())
        medias = self._query_bus.ask(MediaSearchByCriteriaQuery(**criteria))
        response = MediaPaginatedResponseSchema(items=[media.to_primitives() for media in medias])
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
