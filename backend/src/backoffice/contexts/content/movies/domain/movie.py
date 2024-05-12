from src.backoffice.contexts.shared.domain.aggregate_root import AggregateRoot
from src.backoffice.contexts.shared.domain.entity_id import EntityId

from .movie_metadata import MovieMetadata


class Movie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, metadata: MovieMetadata):
        self._id = id
        self._title = title
        self._metadata = metadata

    def get_title(self) -> str:
        return self._title

    def get_metadata(self) -> dict:
        return self._metadata.value

    @classmethod
    def create(cls, title: str, metadata: dict) -> "Movie":
        return cls(EntityId.generate(), title, MovieMetadata(**metadata))

    @classmethod
    def from_primitives(cls, id: EntityId, title: str, metadata: dict) -> "Movie":
        return cls(id, title, MovieMetadata(**metadata))

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "metadata": self._metadata.value}
