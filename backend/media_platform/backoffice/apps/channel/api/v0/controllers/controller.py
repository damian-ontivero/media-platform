from abc import ABCMeta, abstractmethod

from fastapi import Request, Response


class Controller(metaclass=ABCMeta):

    @abstractmethod
    def run(self, request: Request | None) -> Response:
        raise NotImplementedError
