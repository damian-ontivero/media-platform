from fastapi import Request, Response, status

from src.backoffice.contexts.content.movies.application.movie_finder import MovieFinder

from ..schemas import MovieGetSchema
from .controller import Controller


class MovieGetController(Controller):
    def __init__(self, finder: MovieFinder) -> None:
        self._finder = finder

    def run(self, request: Request) -> Response:
        movie = self._finder.run(request.path_params["id"])
        response = MovieGetSchema(**movie.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
