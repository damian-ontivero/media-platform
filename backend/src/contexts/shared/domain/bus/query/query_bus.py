from abc import ABCMeta, abstractmethod

from .query import Query


class QueryBus(metaclass=ABCMeta):
    """
    Interface for query buses.

    Query buses are responsible for asking queries to the appropriate query handler.
    """

    @abstractmethod
    def ask(self, query: Query):
        raise NotImplementedError


class RegisteredQueryError(Exception):
    def __init__(self, query: Query) -> None:
        self._query = query

    def __str__(self) -> str:
        return f"Query: {self._query.__class__.__name__!r} not registered"
