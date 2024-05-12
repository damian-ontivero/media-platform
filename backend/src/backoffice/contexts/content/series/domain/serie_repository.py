from typing import Protocol

from src.backoffice.contexts.shared.domain.criteria import Criteria

from .serie import Serie


class SerieRepository(Protocol):
    def search_all(self) -> list[Serie]: ...
    def search(self, id: str) -> Serie | None: ...
    def matching(self, criteria: Criteria) -> list[Serie]: ...
    def count(self) -> int: ...
    def save(self, beer: Serie) -> None: ...
    def delete(self, id: str) -> None: ...