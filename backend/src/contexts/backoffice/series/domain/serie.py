from src.contexts.backoffice.series.domain.serie_events import SerieCreatedDomainEvent, SerieUpdatedDomainEvent
from src.contexts.backoffice.series.domain.serie_season import SerieSeason, SerieSeasonDict
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.entity_id import EntityId


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

    def __repr__(self) -> str:
        return "{c}(id={id!r}, title={title!r}, seasons={seasons!r})".format(
            c=self.__class__.__name__, id=self._id, title=self._title, seasons=self._seasons
        )

    @classmethod
    def create(cls, title: str, seasons: list[SerieSeasonDict]) -> "Serie":
        serie = cls(EntityId.generate(), title, [SerieSeason.create(**season) for season in seasons])
        serie._ensure_seasons()
        serie.record(SerieCreatedDomainEvent.create(serie.to_primitives()))
        return serie

    @classmethod
    def from_primitives(cls, id: str, title: str, seasons: list[SerieSeasonDict]) -> "Serie":
        return cls(EntityId.from_string(id), title, [SerieSeason.from_primitives(**season) for season in seasons])

    def update(self, title: str, seasons: list[SerieSeasonDict]) -> None:
        self._title = title
        self._seasons = [SerieSeason.create(**season) for season in seasons]
        self._ensure_seasons()
        self.record(SerieUpdatedDomainEvent.create(self.to_primitives()))

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "seasons": [season.to_primitives() for season in self._seasons],
        }

    def _ensure_seasons(self) -> None:
        seasons_numbers = [season.number for season in self._seasons]
        duplicated_seasons = set(
            [season_number for season_number in seasons_numbers if seasons_numbers.count(season_number) > 1]
        )
        if duplicated_seasons:
            raise ValueError("Duplicated seasons: {}".format(", ".join(map(str, duplicated_seasons))))
