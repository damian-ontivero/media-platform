from fastapi import Request, Response, status
from src.backoffice.contexts.channel.content.application.content_finder import ContentFinder

from ..schemas import ContentGetSchema
from .controller import Controller


class ContentGetController(Controller):
    def __init__(self, finder: ContentFinder) -> None:
        self._finder = finder

    def run(self, request: Request) -> Response:
        content = self._finder.run(request.path_params["id"])
        response = ContentGetSchema(**content.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
