from typing import Protocol

from fastapi import Request, Response


class Controller(Protocol):

    def run(self, request: Request | None) -> Response: ...
