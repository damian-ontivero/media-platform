from src.contexts.backoffice.series.application.services import SerieFinder
from src.contexts.backoffice.series.domain import Serie
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .serie_find_by_id_query import SerieFindByIdQuery


class SerieFindByIdQueryHandler(QueryHandler):
    def __init__(self, finder: SerieFinder) -> None:
        self._finder = finder

    @staticmethod
    def subscribed_to() -> Query:
        return SerieFindByIdQuery

    async def handle(self, query: SerieFindByIdQuery) -> Serie:
        return self._finder.run(query.id)
