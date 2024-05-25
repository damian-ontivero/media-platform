from fastapi import Response, status
from src.contexts.backoffice.media.application.media_finder import MediaFinder

from ...schemas import MediaReadSchema
from ..controller import Controller


class MediaGetController(Controller):
    def __init__(self, finder: MediaFinder) -> None:
        self._finder = finder

    def run(self, id: str) -> Response:
        media = self._finder.run(id)
        response = MediaReadSchema(**media.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
