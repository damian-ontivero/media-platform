from typing import TypedDict

from src.contexts.shared.domain import Entity, EntityId

from .serie_episode import SerieEpisode, SerieEpisodeDict


class SerieSeasonDict(TypedDict):
    number: int
    episodes: list[SerieEpisodeDict]


class SerieSeason(Entity):
    def __init__(self, id: EntityId, number: str, episodes: list[SerieEpisode]) -> None:
        super().__init__(id)
        self._number = number
        self._episodes = episodes

    @property
    def number(self) -> str:
        return self._number

    @property
    def episodes(self) -> list[SerieEpisode]:
        return self._episodes

    @classmethod
    def create(cls, number: str, episodes: list[SerieEpisodeDict]) -> "SerieSeason":
        season = cls(EntityId.generate(), number, [SerieEpisode.create(**episode) for episode in episodes])
        return season

    @classmethod
    def from_primitives(cls, id: str, number: str, episodes: list) -> "SerieSeason":
        return cls(EntityId(id), number, [SerieEpisode.from_primitives(**episode) for episode in episodes])

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "number": self._number,
            "episodes": [episode.to_primitives() for episode in self._episodes],
        }
