import abc

from src.contexts.shared.domain.criteria import Criteria

from .serie import Serie


class SerieRepository(abc.ABC):
    """
    Serie repository interface.

    This interface defines the methods that must be provided by the
    repository of series.
    """

    @abc.abstractmethod
    def matching(self, criteria: Criteria) -> list[Serie]:
        raise NotImplementedError

    @abc.abstractmethod
    def search(self, id: str) -> Serie | None:
        raise NotImplementedError

    @abc.abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, beer: Serie) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
