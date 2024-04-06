from media_platform.backoffice.contexts.channel.content.domain import (
    ContentRepository,
)


class ContentUpdater:

    def __init__(self, repository: ContentRepository) -> None:
        self._repository = repository

    def run(
        self,
        id: str,
        files: list[dict],
        rating: float,
        metadata_: dict,
        channel_id: str,
    ) -> None:
        content = self._repository.search(id)
        if content is None:
            raise Exception(f"Content: {id!r} not found")
        content.update(files, rating, metadata_, channel_id)
        self._repository.save(content)
