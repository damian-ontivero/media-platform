from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.domain.criteria import Criteria


class MediaSearcher:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self, filter: dict, sort: list, page_size: int, page_number: int) -> list[Media]:
        criteria = Criteria.from_primitives(filter, sort, page_size, page_number)
        return self._repository.matching(criteria)
