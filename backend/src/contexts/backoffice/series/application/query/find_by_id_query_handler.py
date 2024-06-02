from src.contexts.backoffice.series.domain.serie import Serie
from src.contexts.backoffice.series.domain.serie_repository import SerieRepository
from src.contexts.shared.domain import EntityNotFound
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import SerieFindByIdQuery


class SerieFindByIdQueryHandler(QueryHandler):
    def __init__(self, repository: SerieRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return SerieFindByIdQuery

    def handle(self, query: SerieFindByIdQuery) -> Serie:
        serie = self.repository.search(query.id)
        if serie is None:
            raise EntityNotFound(f"Serie: {query.id!r} not found")
        return serie
