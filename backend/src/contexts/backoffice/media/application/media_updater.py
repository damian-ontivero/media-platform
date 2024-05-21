from src.contexts.backoffice.media.domain import MediaRepository


class MediaUpdater:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self, id: str, files: list[dict], rating: float, metadata_: dict, channel_id: str) -> None:
        media = self._repository.search(id)
        if media is None:
            raise Exception(f"Media: {id!r} not found")
        media.update(files, rating, metadata_, channel_id)
        self._repository.save(media)
