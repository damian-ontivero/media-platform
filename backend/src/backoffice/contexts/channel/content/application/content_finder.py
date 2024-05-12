from src.backoffice.contexts.channel.content.domain import Content, ContentRepository


class ContentFinder:
    def __init__(self, repository: ContentRepository) -> None:
        self.repository = repository

    def run(self, id: str) -> Content:
        content = self.repository.search(id)
        if content is None:
            raise ValueError(f"Content: {id!r} not found")
        return content
