from src.contexts.catalog.media.domain import Media, MediaDoesNotExist, MediaRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import MediaFindByIdQuery


class MediaFindByIdQueryHandler(QueryHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def subscribed_to(self) -> Query:
        return MediaFindByIdQuery

    async def handle(self, query: MediaFindByIdQuery) -> Media:
        media = self._repository.search(query.id)
        if media is None:
            raise MediaDoesNotExist(f"Media with id {query.id!r} does not exist")
        return media
