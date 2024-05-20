from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.domain.criteria import Criteria


class MediaSearcher:
    def __init__(self, repository: MediaRepository) -> None:
        self.repository = repository

    def run(self, criteria: dict | None = None) -> list[Media]:
        if criteria is None:
            return self.repository.search_all()
        return self.repository.matching(Criteria.from_primitives(**criteria))
