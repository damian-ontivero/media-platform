from abc import ABC, abstractmethod

from .query import Query


class QueryBus(ABC):
    """
    Interface for query buses.

    Query buses are responsible for asking queries to the appropriate query handler.
    """

    @abstractmethod
    async def ask(self, query: Query):
        raise NotImplementedError


class QueryHandlerNotFound(Exception):
    pass
