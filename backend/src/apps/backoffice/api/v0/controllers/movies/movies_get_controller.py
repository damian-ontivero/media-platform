import base64
import json

from fastapi import Response, status
from src.contexts.backoffice.movies.application.query.search_by_criteria_query import MovieSearchByCriteriaQuery
from src.contexts.shared.domain.bus.query import QueryBus

from ...schemas import MoviePaginatedResponseSchema
from ..controller import Controller


class MoviesGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    def run(self, criteria: str | None) -> Response:
        if criteria is None:
            criteria = {"filter": {}, "sort": [], "page_size": 10, "page_number": 1}
            criteria = base64.b64encode(json.dumps(criteria).encode()).decode()
        criteria = json.loads(base64.b64decode(criteria).decode())
        movies = self._query_bus.ask(MovieSearchByCriteriaQuery(**criteria))
        response = MoviePaginatedResponseSchema(items=[movie.to_primitives() for movie in movies])
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
