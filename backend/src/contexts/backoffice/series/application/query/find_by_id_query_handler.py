from src.contexts.backoffice.series.domain import Serie, SerieDoesNotExist, SerieRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import SerieFindByIdQuery


class SerieFindByIdQueryHandler(QueryHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return SerieFindByIdQuery

    async def handle(self, query: SerieFindByIdQuery) -> Serie:
        serie = self.repository.search(query.id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {query.id!r} does not exist")
        return serie
