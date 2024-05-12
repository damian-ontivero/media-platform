from typing import Protocol

from src.backoffice.contexts.shared.domain.criteria import Criteria

from .channel import Channel


class ChannelRepository(Protocol):
    def search_all(self) -> list[Channel]: ...
    def search(self, id: str) -> Channel | None: ...
    def matching(self, criteria: Criteria) -> list[Channel]: ...
    def count(self) -> int: ...
    def save(self, beer: Channel) -> None: ...
    def delete(self, id: str) -> None: ...