from src.contexts.catalog.series.domain import Serie, SerieDoesNotExist, SerieRepository


class SerieFinder:
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Serie:
        serie = self._repository.search(id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {id!r} does not exist")
        return serie
