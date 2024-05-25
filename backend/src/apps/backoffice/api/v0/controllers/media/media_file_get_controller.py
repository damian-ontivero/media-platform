import os

from fastapi import Response, status
from src.contexts.backoffice.media.application.media_finder import MediaFinder

from ..controller import Controller


class MediaFileGetController(Controller):
    def __init__(self, finder: MediaFinder) -> None:
        self._finder = finder

    async def run(self, id: str, range: str) -> Response:
        media = self._finder.run(id)
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
