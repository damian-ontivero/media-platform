from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.criteria import Criteria

from .media_search_by_criteria_query import MediaSearchByCriteriaQuery


class MediaSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Query:
        return MediaSearchByCriteriaQuery

    async def handle(self, query: MediaSearchByCriteriaQuery) -> list[Media]:
        criteria = Criteria.from_primitives(query.filter, query.sort, query.page_size, query.page_number)
        return self._repository.matching(criteria)
