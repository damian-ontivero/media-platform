from typing import TypedDict

from src.contexts.shared.domain import Entity, EntityId


class SerieEpisodeDict(TypedDict):
    number: int
    title: str
    duration: int


class SerieEpisode(Entity):
    def __init__(self, id: EntityId, number: str, title: str, media_id: EntityId) -> None:
        super().__init__(id)
        self._number = number
        self._title = title
        self._media_id = media_id

    @property
    def number(self) -> str:
        return self._number

    @property
    def title(self) -> str:
        return self._title

    @property
    def media_id(self) -> EntityId:
        return self._media_id

    @classmethod
    def create(cls, number: str, title: str, media_id: str) -> "SerieEpisode":
        episode = cls(EntityId.generate(), number, title, EntityId(media_id))
        return episode

    @classmethod
    def from_primitives(cls, id: str, number: str, title: str, media_id: str) -> "SerieEpisode":
        return cls(EntityId(id), number, title, EntityId(media_id))

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "number": self._number, "title": self._title, "media_id": self._media_id.value}
