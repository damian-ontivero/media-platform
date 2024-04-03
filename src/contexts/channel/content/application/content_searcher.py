from src.contexts.channel.content.domain import Content, ContentRepository
from src.contexts.shared.domain.criteria import Criteria


class ContentSearcher:

    def __init__(self, repository: ContentRepository) -> None:
        self.repository = repository

    def run(self, criteria: dict | None = None) -> list[Content]:
        if criteria is None:
            content = self.repository.search_all()
            return content
        content = self.repository.matching(
            Criteria.from_primitives(**criteria)
        )
        return content
