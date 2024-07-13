from fastapi import Response, status
from src.apps.catalog.api.v0.schemas import SerieReadSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.catalog.series.application.services import SerieFinder


class SerieGetController(Controller):
    def __init__(self, finder: SerieFinder) -> None:
        self._finder = finder

    async def run(self, id: str) -> Response:
        serie = self._finder.run(id)
        response = SerieReadSchema(**serie.to_primitives())
        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
