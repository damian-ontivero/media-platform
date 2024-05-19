class SerieEpisode:
    def __init__(self, number: int, title: str) -> None:
        self._number = number
        self._title = title

    @property
    def number(self) -> int:
        return self._number

    @property
    def title(self) -> str:
        return self._title

    @classmethod
    def create(cls, number: int, title: str) -> "SerieEpisode":
        episode = cls(number, title)
        return episode

    @classmethod
    def from_primitives(cls, number: int, title: str) -> "SerieEpisode":
        return cls(number, title)

    def to_primitives(self) -> dict:
        return {"number": self._number, "title": self._title}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SerieEpisode):
            return NotImplemented
        return self._number == other._number and self._title == other._title

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(tuple(sorted(self._number, self._title)))

    def __repr__(self) -> str:
        return f"SerieEpisode(number={self._number}, title={self._title})"
