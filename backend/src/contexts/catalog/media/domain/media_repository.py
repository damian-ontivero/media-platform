import abc

from src.contexts.shared.domain.criteria import Criteria

from .media import Media


class MediaRepository(abc.ABC):
    """
    Media repository interface.

    This interface defines the methods that must be provided by the
    repository of media.
    """

    @abc.abstractmethod
    def matching(self, criteria: Criteria) -> list[Media]:
        raise NotImplementedError

    @abc.abstractmethod
    def search(self, id: str) -> Media | None:
        raise NotImplementedError

    @abc.abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, beer: Media) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
