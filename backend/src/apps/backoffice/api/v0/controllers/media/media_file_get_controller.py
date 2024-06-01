import os

from fastapi import Response, status
from src.contexts.backoffice.media.application.query.find_by_id_query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.query import QueryBus

from ..controller import Controller


class MediaFileGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    async def run(self, id: str, range: str) -> Response:
        media = self._query_bus.ask(MediaFindByIdQuery(id))
        start, end = range.replace("bytes=", "").split("-")
        start = int(start)
        end = int(start + (1024 * 1024))

        with open(media.path, "rb") as f:
            f.seek(start)
            data = f.read(end - start)
            response = Response(
                content=data,
                status_code=status.HTTP_206_PARTIAL_CONTENT,
                headers={
                    "Content-Range": f"bytes {start}-{end}/{os.path.getsize(media.path)}",
                    "Content-Length": str(len(data)),
                },
            )
            return response
