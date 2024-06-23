from src.contexts.shared.domain import AggregateRoot, EntityId

from .serie_season import SerieSeason, SerieSeasonDict


class Serie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, seasons: list[SerieSeason]) -> None:
        super().__init__(id)
        self._title = title
        self._seasons = seasons
        self._ensure_seasons()

    @property
    def title(self) -> str:
        return self._title

    @property
    def seasons(self) -> list[SerieSeason]:
        return self._seasons

    @classmethod
    def create(cls, title: str, seasons: list[SerieSeasonDict]) -> "Serie":
        serie = cls(EntityId.generate(), title, [SerieSeason.create(**season) for season in seasons])
        return serie

    @classmethod
    def from_primitives(cls, id: str, title: str, seasons: list[SerieSeasonDict]) -> "Serie":
        return cls(EntityId.from_string(id), title, [SerieSeason.from_primitives(**season) for season in seasons])

    def update(self, title: str, seasons: list[SerieSeasonDict]) -> None:
        self._title = title
        self._seasons = [SerieSeason.create(**season) for season in seasons]

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "seasons": [season.to_primitives() for season in self._seasons],
        }

    def _ensure_seasons(self) -> None:
        import ipdb

        ipdb.set_trace()
        duplicated_seasons = [season for season in self._seasons if self._seasons.count(season) > 1]
        if duplicated_seasons:
            raise ValueError(f"Seasons {duplicated_seasons} are duplicated")
