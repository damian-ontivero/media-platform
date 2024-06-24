from abc import ABC, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .movie import Movie


class MovieRepository(ABC):
    """
    Movie repository interface.

    This interface defines the methods that must be provided by the
    repository of movies.
    """

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Movie]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Movie | None:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Movie) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
