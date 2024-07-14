from src.contexts.backoffice.media.application.services import MediaSearcher
from src.contexts.backoffice.media.domain import Media
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .media_search_by_criteria_query import MediaSearchByCriteriaQuery


class MediaSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, searcher: MediaSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> Query:
        return MediaSearchByCriteriaQuery

    async def handle(self, query: MediaSearchByCriteriaQuery) -> list[Media]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
