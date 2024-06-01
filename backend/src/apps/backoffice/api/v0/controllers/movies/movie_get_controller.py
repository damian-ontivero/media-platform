from fastapi import Response, status
from src.contexts.backoffice.movies.application.query.find_by_id_query import MovieFindByIdQuery
from src.contexts.shared.domain.bus.query import QueryBus

from ...schemas import MovieReadSchema
from ..controller import Controller


class MovieGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    def run(self, id: str) -> Response:
        movie = self._query_bus.ask(MovieFindByIdQuery(id))
        response = MovieReadSchema(**movie.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
