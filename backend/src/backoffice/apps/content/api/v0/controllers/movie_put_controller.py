from fastapi import Request, Response, status

from src.backoffice.contexts.content.movies.application.movie_updater import MovieUpdater

from .controller import Controller


class MoviePutController(Controller):
    def __init__(self, updater: MovieUpdater) -> None:
        self._updater = updater

    async def run(self, request: Request) -> Response:
        data = await request.json()
        self._updater.run(id=request.path_params["id"], title=data["title"], metadata=data["metadata"])
        return Response(content=None, status_code=status.HTTP_200_OK, media_type="application/json")
