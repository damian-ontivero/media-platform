from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import MediaFindByIdQuery


class MediaFindByIdQueryHandler(QueryHandler):
    def __init__(self, repository: MediaRepository) -> None:
        self.repository = repository

    def subscribed_to(self) -> Query:
        return MediaFindByIdQuery

    def handle(self, query: MediaFindByIdQuery) -> Media:
        media = self.repository.search(query.id)
        if media is None:
            raise ValueError(f"Media: {query.id!r} not found")
        return media
