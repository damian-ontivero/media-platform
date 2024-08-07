import base64
import json

from fastapi import Response
from fastapi import status

from src.apps.backoffice.api.v0.schemas.series import SeriePaginatedResponseSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.series.application.queries.serie_count_query import SerieCountQuery
from src.contexts.backoffice.series.application.queries.serie_search_by_criteria_query import SerieSearchByCriteriaQuery
from src.contexts.shared.domain.query_bus.query_bus import QueryBus


class SeriesGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    async def run(self, criteria: str | None) -> Response:
        if criteria is None:
            criteria = {"filter": {}, "sort": [], "page_size": 10, "page_number": 1}
            criteria = base64.b64encode(json.dumps(criteria).encode()).decode()
        criteria = json.loads(base64.b64decode(criteria).decode())
        series = await self._query_bus.ask(SerieSearchByCriteriaQuery(**criteria))
        total = await self._query_bus.ask(SerieCountQuery())
        response = SeriePaginatedResponseSchema(
            page_size=criteria["page_size"],
            page_number=criteria["page_number"],
            total_pages=total // criteria["page_size"],
            items=[serie.to_primitives() for serie in series],
        )
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
