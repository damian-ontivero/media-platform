from abc import ABC, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .media import Media


class MediaRepository(ABC):
    """
    Media repository interface.

    This interface defines the methods that must be provided by the
    repository of media.
    """

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Media]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Media | None:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Media) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
