from src.contexts.catalog.media.domain import Media, MediaDoesNotExist, MediaRepository


class MediaFinder:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Media:
        media = self._repository.search(id)
        if media is None:
            raise MediaDoesNotExist(f"Media with id {id!r} does not exist")
        return media
