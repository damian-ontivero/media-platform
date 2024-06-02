from fastapi import Response, status
from src.apps.backoffice.api.v0.schemas import SerieReadSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.series.application.query.find_by_id_query import SerieFindByIdQuery
from src.contexts.shared.domain.bus.query import QueryBus


class SerieGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    def run(self, id: str) -> Response:
        serie = self._query_bus.ask(SerieFindByIdQuery(id))
        response = SerieReadSchema(**serie.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )