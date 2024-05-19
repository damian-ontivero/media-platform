from src.backoffice.contexts.shared.domain.aggregate_root import AggregateRoot
from src.backoffice.contexts.shared.domain.entity_id import EntityId

from .serie_season import SerieSeason


class Serie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, seasons: list[SerieSeason]) -> None:
        super().__init__(id)
        self._title = title
        self._seasons = seasons

    @property
    def title(self) -> str:
        return self._title

    @property
    def seasons(self) -> list[SerieSeason]:
        return self._seasons

    @classmethod
    def create(cls, title: str, seasons: list) -> "Serie":
        serie = cls(EntityId.generate(), title, seasons)
        return serie

    @classmethod
    def from_primitives(cls, id: str, title: str, seasons: list) -> "Serie":
        return cls(EntityId(id), title, seasons)

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "seasons": self._seasons.to_primitives()}
