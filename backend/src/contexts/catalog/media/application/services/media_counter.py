from src.contexts.catalog.media.domain import MediaRepository


class MediaCounter:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self) -> int:
        return self._repository.count()
