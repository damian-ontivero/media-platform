from fastapi import Response, status

from src.apps.backoffice.api.v0.schemas import MediaReadSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.query import QueryBus


class MediaGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    def run(self, id: str) -> Response:
        media = self._query_bus.ask(MediaFindByIdQuery(id))
        response = MediaReadSchema(**media.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
