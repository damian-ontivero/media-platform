from fastapi import Response, status
from src.contexts.backoffice.movies.application.movie_eliminator import MovieEliminator

from ..controller import Controller


class MovieDeleteController(Controller):
    def __init__(self, eliminator: MovieEliminator) -> None:
        self._eliminator = eliminator

    async def run(self, id: str) -> Response:
        self._eliminator.run(id)
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
