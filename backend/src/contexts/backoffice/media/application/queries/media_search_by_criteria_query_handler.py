from src.contexts.backoffice.media.application.queries.media_search_by_criteria_query import MediaSearchByCriteriaQuery
from src.contexts.backoffice.media.application.services.media_searcher import MediaSearcher
from src.contexts.backoffice.media.domain.media import Media
from src.contexts.shared.domain.query_bus.query import Query
from src.contexts.shared.domain.query_bus.query_handler import QueryHandler


class MediaSearchByCriteriaQueryHandler(QueryHandler):
    def __init__(self, searcher: MediaSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> Query:
        return MediaSearchByCriteriaQuery

    async def handle(self, query: MediaSearchByCriteriaQuery) -> list[Media]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
