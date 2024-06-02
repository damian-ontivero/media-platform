from abc import ABC, abstractmethod

from fastapi import Request, Response


class Controller(ABC):
    """
    Controller interface.

    This interface defines the methods that must be provided by the
    controllers.
    """

    @abstractmethod
    def run(self, request: Request | None) -> Response:
        raise NotImplementedError
