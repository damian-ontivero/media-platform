from fastapi import Response
from fastapi import status

from src.apps.backoffice.api.v0.schemas.series import SerieReadSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.series.application.queries.serie_find_by_id_query import SerieFindByIdQuery
from src.contexts.shared.domain.query_bus.query_bus import QueryBus


class SerieGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    async def run(self, id: str) -> Response:
        serie = await self._query_bus.ask(SerieFindByIdQuery(id))
        response = SerieReadSchema(**serie.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
