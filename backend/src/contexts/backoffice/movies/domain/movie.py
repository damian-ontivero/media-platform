from src.contexts.shared.domain import AggregateRoot, EntityId, VideoLink


class Movie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, media_id: EntityId) -> None:
        super().__init__(id)
        self._title = title
        self._media_id = media_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def media_id(self) -> EntityId:
        return self._media_id

    @classmethod
    def create(cls, title: str, media_id: str) -> "Movie":
        movie = cls(EntityId.generate(), title, EntityId(media_id))
        return movie

    @classmethod
    def from_primitives(cls, id: str, title: str, media_id: str) -> "Movie":
        return cls(EntityId(id), title, EntityId(media_id))

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "media_id": self._media_id.value}
