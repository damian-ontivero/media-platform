from src.contexts.backoffice.media.application.services import MediaFinder
from src.contexts.backoffice.media.domain import Media
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.query import Query, QueryHandler


class MediaFindByIdQueryHandler(QueryHandler):
    def __init__(self, finder: MediaFinder) -> None:
        self._finder = finder

    def subscribed_to(self) -> Query:
        return MediaFindByIdQuery

    async def handle(self, query: MediaFindByIdQuery) -> Media:
        return self._finder.run(query.id)
