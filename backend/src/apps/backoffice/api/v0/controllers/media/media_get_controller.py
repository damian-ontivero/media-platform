from fastapi import Response, status
from src.contexts.backoffice.media.application.query.find_by_id_query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.query import QueryBus

from ...schemas import MediaReadSchema
from ..controller import Controller


class MediaGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    def run(self, id: str) -> Response:
        media = self._query_bus.ask(MediaFindByIdQuery(id))
        response = MediaReadSchema(**media.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
