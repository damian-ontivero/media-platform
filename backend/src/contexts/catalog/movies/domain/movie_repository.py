import abc

from src.contexts.shared.domain.criteria import Criteria

from .movie import Movie


class MovieRepository(abc.ABC):
    """
    Movie repository interface.

    This interface defines the methods that must be provided by the
    repository of movies.
    """

    @abc.abstractmethod
    def matching(self, criteria: Criteria) -> list[Movie]:
        raise NotImplementedError

    @abc.abstractmethod
    def search(self, id: str) -> Movie | None:
        raise NotImplementedError

    @abc.abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, beer: Movie) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
