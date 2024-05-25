from fastapi import Response, status
from src.contexts.backoffice.movies.application.movie_updater import MovieUpdater

from ...schemas import MovieWriteSchema
from ..controller import Controller


class MoviePutController(Controller):
    def __init__(self, updater: MovieUpdater) -> None:
        self._updater = updater

    async def run(self, id: str, movie: MovieWriteSchema) -> Response:
        self._updater.run(id=id, **movie.model_json_schema())
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
