import base64
import json

from fastapi import Response, status

from src.apps.catalog.api.v0.schemas.movies import MoviePaginatedResponseSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.catalog.movies.application.services.movie_counter import MovieCounter
from src.contexts.catalog.movies.application.services.movie_searcher import MovieSearcher


class MoviesGetController(Controller):
    def __init__(self, searcher: MovieSearcher, counter: MovieCounter) -> None:
        self._searcher = searcher
        self._counter = counter

    async def run(self, criteria: str | None) -> Response:
        if criteria is None:
            criteria = {"filter": {}, "sort": [], "page_size": 10, "page_number": 1}
            criteria = base64.b64encode(json.dumps(criteria).encode()).decode()
        criteria = json.loads(base64.b64decode(criteria).decode())
        movies = self._searcher.run(criteria)
        total = self._counter.run()
        response = MoviePaginatedResponseSchema(
            page_size=criteria["page_size"],
            page_number=criteria["page_number"],
            total_pages=total // criteria["page_size"],
            items=[movie.to_primitives() for movie in movies],
        )
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
