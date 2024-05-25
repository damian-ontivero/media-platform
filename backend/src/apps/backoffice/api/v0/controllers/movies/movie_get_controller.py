from fastapi import Response, status
from src.contexts.backoffice.movies.application.movie_finder import MovieFinder

from ...schemas import MovieReadSchema
from ..controller import Controller


class MovieGetController(Controller):
    def __init__(self, finder: MovieFinder) -> None:
        self._finder = finder

    def run(self, id: str) -> Response:
        movie = self._finder.run(id)
        response = MovieReadSchema(**movie.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
