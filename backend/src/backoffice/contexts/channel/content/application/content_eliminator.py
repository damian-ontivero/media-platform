from src.backoffice.contexts.channel.content.domain import ContentRepository


class ContentEliminator:
    def __init__(self, repository: ContentRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> None:
        content = self._repository.search(id)
        if content is None:
            raise Exception(f"Content: {id!r} not found")
        self._repository.delete(id)
