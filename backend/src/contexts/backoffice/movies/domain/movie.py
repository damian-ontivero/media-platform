from src.contexts.backoffice.movies.domain.movie_events import MovieCreatedDomainEvent, MovieUpdatedDomainEvent
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.entity_id import EntityId


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

    def __repr__(self) -> str:
        return "{c}(id={id!r}, title={title!r}, media_id={media_id!r})".format(
            c=self.__class__.__name__, id=self._id, title=self._title, media_id=self._media_id
        )

    @classmethod
    def create(cls, title: str, media_id: str) -> "Movie":
        movie = cls(EntityId.generate(), title, EntityId.from_string(media_id))
        movie.record(MovieCreatedDomainEvent.create(movie.to_primitives()))
        return movie

    @classmethod
    def from_primitives(cls, id: str, title: str, media_id: str) -> "Movie":
        return cls(EntityId.from_string(id), title, EntityId.from_string(media_id))

    def update(self, title: str, media_id: str) -> None:
        self._title = title
        self._media_id = EntityId.from_string(media_id)
        self.record(MovieUpdatedDomainEvent.create(self.to_primitives()))

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "media_id": self._media_id.value}
