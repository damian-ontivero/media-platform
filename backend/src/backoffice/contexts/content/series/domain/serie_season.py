from .serie_episode import SerieEpisode


class SerieSeason:
    def __init__(self, number: int, episodes: list[SerieEpisode]) -> None:
        self._number = number
        self._episodes = episodes

    @property
    def number(self) -> int:
        return self._number

    @property
    def episodes(self) -> list[SerieEpisode]:
        return self._episodes

    @classmethod
    def create(cls, number: int, episodes: list) -> "SerieSeason":
        season = cls(number, [SerieEpisode.create(episode) for episode in episodes])
        return season

    @classmethod
    def from_primitives(cls, number: int, episodes: list) -> "SerieSeason":
        return cls(number, [SerieEpisode.from_primitives(episode) for episode in episodes])

    def to_primitives(self) -> dict:
        return {"number": self._number, "episodes": [episode.to_primitives() for episode in self._episodes]}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SerieSeason):
            return NotImplemented
        return self._number == other._number and self._episodes == other._episodes

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(tuple(sorted(self._number, self._episodes)))

    def __repr__(self) -> str:
        return f"SerieSeason(number={self._number}, episodes={self._episodes})"
