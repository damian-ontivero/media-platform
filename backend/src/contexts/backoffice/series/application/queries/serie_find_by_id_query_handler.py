from src.contexts.backoffice.series.application.queries.serie_find_by_id_query import SerieFindByIdQuery
from src.contexts.backoffice.series.application.services.serie_finder import SerieFinder
from src.contexts.backoffice.series.domain.serie import Serie
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class SerieFindByIdQueryHandler(QueryHandler):
    def __init__(self, finder: SerieFinder) -> None:
        self._finder = finder

    @staticmethod
    def subscribed_to() -> Query:
        return SerieFindByIdQuery

    async def handle(self, query: SerieFindByIdQuery) -> Serie:
        return self._finder.run(query.id)
