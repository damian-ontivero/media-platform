from fastapi import Request, Response, status

from src.backoffice.contexts.content.movies.application.movie_eliminator import MovieEliminator

from .controller import Controller


class MovieDeleteController(Controller):
    def __init__(self, eliminator: MovieEliminator) -> None:
        self._eliminator = eliminator

    async def run(self, request: Request) -> Response:
        self._eliminator.run(request.path_params["id"])
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
