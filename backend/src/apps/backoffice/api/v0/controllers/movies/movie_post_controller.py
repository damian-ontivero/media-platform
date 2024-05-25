from fastapi import Response, status
from src.contexts.backoffice.movies.application.movie_creator import MovieCreator

from ...schemas import MovieWriteSchema
from ..controller import Controller


class MoviePostController(Controller):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    async def run(self, movie: MovieWriteSchema) -> Response:
        self._creator.run(**movie.model_json_schema())
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type="application/json")
