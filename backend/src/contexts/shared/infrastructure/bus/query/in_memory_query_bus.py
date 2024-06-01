from src.contexts.shared.domain.bus.query import Query, QueryBus, QueryHandler, RegisteredQueryError


class InMemoryQueryBus(QueryBus):
    def __init__(self, query_handlers: list[QueryHandler]) -> None:
        self._query_handler_map = {query_handler.subscribed_to(): query_handler for query_handler in query_handlers}

    def ask(self, query: Query):
        handler = self._query_handler_map.get(type(query))
        if handler is None:
            raise RegisteredQueryError(f"Query handler not found for {query.__class__.__name__}")
        return handler.handle(query)
