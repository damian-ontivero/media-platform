from src.contexts.backoffice.media.domain import MediaRepository


class MediaEliminator:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> None:
        media = self._repository.search(id)
        if media is None:
            raise Exception(f"Media: {id!r} not found")
        self._repository.delete(id)
