from abc import ABCMeta, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .content import Content


class ContentRepository(metaclass=ABCMeta):

    @abstractmethod
    def search_all(self) -> list[Content]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Content | None:
        raise NotImplementedError

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Content]:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Content) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
