import os

from fastapi import Request, Response, status
from media_platform.backoffice.contexts.channel.content.application.content_finder import (
    ContentFinder,
)

from .controller import Controller


class ContentFileGetController(Controller):

    def __init__(self, finder: ContentFinder) -> None:
        self._finder = finder

    async def run(self, request: Request) -> Response:
        content = self._finder.run(request.path_params["id"])
        range = request.headers.get("Range")
        start, end = range.replace("bytes=", "").split("-")
        start = int(start)
        end = int(start + (1024 * 1024))

        for file in content.files:
            if file.name == request.query_params["file_name"]:
                with open(file.path, "rb") as f:
                    f.seek(start)
                    data = f.read(end - start)
                    response = Response(
                        content=data,
                        status_code=status.HTTP_206_PARTIAL_CONTENT,
                        headers={
                            "Content-Range": f"bytes {start}-{end}/{os.path.getsize(file.path)}",
                            "Content-Length": str(len(data)),
                        },
                    )
                    return response
