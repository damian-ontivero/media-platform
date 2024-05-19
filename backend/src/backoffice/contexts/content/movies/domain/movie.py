from src.backoffice.contexts.shared.domain import AggregateRoot, EntityId, VideoLink


class Movie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, links: list[VideoLink]) -> None:
        super().__init__(id)
        self._title = title
        self._links = links

    @property
    def title(self) -> str:
        return self._title

    @property
    def links(self) -> list[VideoLink]:
        return self._links

    @classmethod
    def create(cls, title: str, links: list[str]) -> "Movie":
        movie = cls(EntityId.generate(), title, [VideoLink(link) for link in links])
        return movie

    @classmethod
    def from_primitives(cls, id: str, title: str, links: list[str]) -> "Movie":
        return cls(EntityId(id), title, [VideoLink(link) for link in links])

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "links": [link.value for link in self._links]}
