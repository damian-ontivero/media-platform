import abc

from .query import Query


class QueryHandler(abc.ABC):
    """
    Interface for query handlers.

    Query handlers are responsible for handling queries that are asked
    by the query bus. They contain the business logic that is executed when
    a query is asked.

    Query handlers are subscribed to the queries they handle. When a query
    is asked, the query bus will find the appropriate query handler
    and call its ask method.
    """

    @abc.abstractmethod
    def subscribed_to(self) -> Query:
        raise NotImplementedError

    @abc.abstractmethod
    async def handle(self, query: Query):
        raise NotImplementedError
