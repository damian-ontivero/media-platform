import json

from fastapi import Request, Response, status
from src.backoffice.contexts.content.movies.application.movie_creator import MovieCreator

from .controller import Controller


class MoviePostController(Controller):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    async def run(self, request: Request) -> Response:
        data = await request.form()
        files = []
        for file in data.getlist("files"):
            files.append({"name": file.filename, "data": file.file.read(), "media_type": file.content_type})
        self._creator.run(title=data["title"], metadata=json.loads(data["metadata"]))
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type="application/json")
