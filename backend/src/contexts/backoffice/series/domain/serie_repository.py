from abc import ABC, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .serie import Serie


class SerieRepository(ABC):
    """
    Serie repository interface.

    This interface defines the methods that must be provided by the
    repository of series.
    """

    @abstractmethod
    def search_all(self) -> list[Serie]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Serie | None:
        raise NotImplementedError

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Serie]:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Serie) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
