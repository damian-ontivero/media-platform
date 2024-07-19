from src.contexts.backoffice.series.domain.serie import Serie
from src.contexts.backoffice.series.domain.serie_exceptions import SerieDoesNotExist
from src.contexts.backoffice.series.domain.serie_repository import SerieRepository


class SerieFinder:
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Serie:
        serie = self._repository.search(id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {id!r} does not exist")
        return serie
