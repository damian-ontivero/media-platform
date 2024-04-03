from abc import ABCMeta, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .channel import Channel


class ChannelRepository(metaclass=ABCMeta):

    @abstractmethod
    def search_all(self) -> list[Channel]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Channel | None:
        raise NotImplementedError

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Channel]:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Channel) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
