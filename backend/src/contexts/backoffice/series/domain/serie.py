from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.entity_id import EntityId

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
        serie = cls(EntityId.generate(), title, [SerieSeason.create(**season) for season in seasons])
        return serie

    @classmethod
    def from_primitives(cls, id: str, title: str, seasons: list) -> "Serie":
        return cls(EntityId(id), title, [SerieSeason.from_primitives(**season) for season in seasons])

    def update(self, title: str, seasons: list) -> None:
        self._title = title
        self._seasons = [SerieSeason.create(**season) for season in seasons]

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "seasons": [season.to_primitives() for season in self._seasons],
        }
