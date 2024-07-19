import base64
import json

from fastapi import Response, status
from src.apps.catalog.api.v0.schemas.series import SeriePaginatedResponseSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.catalog.series.application.services.serie_counter import SerieCounter
from src.contexts.catalog.series.application.services.serie_searcher import SerieSearcher


class SeriesGetController(Controller):
    def __init__(self, searcher: SerieSearcher, counter: SerieCounter) -> None:
        self._searcher = searcher
        self._counter = counter

    async def run(self, criteria: str | None) -> Response:
        if criteria is None:
            criteria = {"filter": {}, "sort": [], "page_size": 10, "page_number": 1}
            criteria = base64.b64encode(json.dumps(criteria).encode()).decode()
        criteria = json.loads(base64.b64decode(criteria).decode())
        series = self._searcher.run(criteria)
        total = self._counter.run()
        response = SeriePaginatedResponseSchema(
            page_size=criteria["page_size"],
            page_number=criteria["page_number"],
            total_pages=total // criteria["page_size"],
            items=[serie.to_primitives() for serie in series],
        )
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
