import abc

from .query import Query


class QueryBus(abc.ABC):
    """
    Interface for query buses.

    Query buses are responsible for asking queries to the appropriate query handler.
    """

    @abc.abstractmethod
    async def ask(self, query: Query):
        raise NotImplementedError


class QueryHandlerNotFound(Exception):
    pass
