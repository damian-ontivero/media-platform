from src.backoffice.contexts.shared.domain.aggregate_root import AggregateRoot
from src.backoffice.contexts.shared.domain.entity_id import EntityId

from .movie_metada import SerieMetadata


class Serie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, metadata: SerieMetadata):
        self._id = id
        self._title = title
        self._metadata = metadata

    def get_title(self) -> str:
        return self._title

    def get_metadata(self) -> dict:
        return self._metadata.value

    @classmethod
    def create(cls, title: str, metadata: dict) -> "Serie":
        return cls(EntityId.generate(), title, SerieMetadata(**metadata))

    @classmethod
    def from_primitives(cls, id: EntityId, title: str, metadata: dict) -> "Serie":
        return cls(id, title, SerieMetadata(**metadata))

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "metadata": self._metadata.value}
