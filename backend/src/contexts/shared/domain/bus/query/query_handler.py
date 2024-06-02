from abc import ABC, abstractmethod

from .query import Query


class QueryHandler(ABC):
    """
    Interface for query handlers.

    Query handlers are responsible for handling queries that are asked
    by the query bus. They contain the business logic that is executed when
    a query is asked.

    Query handlers are subscribed to the queries they handle. When a query
    is asked, the query bus will find the appropriate query handler
    and call its ask method.
    """

    @abstractmethod
    def subscribed_to(self) -> Query:
        raise NotImplementedError

    @abstractmethod
    def handle(self, query: Query):
        raise NotImplementedError
