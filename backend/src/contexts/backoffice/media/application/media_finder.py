from src.contexts.backoffice.media.domain import Media, MediaRepository


class MediaFinder:
    def __init__(self, repository: MediaRepository) -> None:
        self.repository = repository

    def run(self, id: str) -> Media:
        media = self.repository.search(id)
        if media is None:
            raise ValueError(f"Media: {id!r} not found")
        return media
