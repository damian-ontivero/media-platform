import base64
import json

from fastapi import Request, Response, status
from src.contexts.backoffice.movies.application.movie_searcher import MovieSearcher

from ...schemas import MoviePaginatedResponseSchema
from ..controller import Controller


class MoviesGetController(Controller):
    def __init__(self, searcher: MovieSearcher) -> None:
        self._searcher = searcher

    def run(self, criteria: str | None) -> Response:
        if criteria is not None:
            criteria = json.loads(base64.b64decode(criteria).decode())
        movies = self._searcher.run(criteria)
        response = MoviePaginatedResponseSchema(items=[movie.to_primitives() for movie in movies])
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
