import abc

from fastapi import Response


class Controller(abc.ABC):
    """
    Controller interface.

    This interface defines the methods that must be provided by the
    controllers.
    """

    @abc.abstractmethod
    async def run(self, *args, **kwargs) -> Response:
        raise NotImplementedError
