from src.contexts.shared.domain import AggregateRoot, EntityId


class Media(AggregateRoot):
    def __init__(self, id: EntityId, title: str, size: int, duration: int, path: str) -> None:
        self._id = id
        self._title = title
        self._size = size
        self._duration = duration
        self._path = path

    @property
    def title(self) -> str:
        return self._title

    @property
    def size(self) -> int:
        return self._size

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def path(self) -> str:
        return self._path

    @classmethod
    def create(cls, title: str, size: int, duration: int, path: str) -> "Media":
        media = cls(EntityId.generate(), title, size, duration, path)
        return media

    @classmethod
    def from_primitives(cls, id: str, title: str, size: int, duration: int, path: str) -> "Media":
        return cls(EntityId(id), title, size, duration, path)

    def update(self, title: str, size: int, duration: int, path: str) -> None:
        self._title = title
        self._size = size
        self._duration = duration
        self._path = path

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "size": self._size,
            "duration": self._duration,
            "path": self._path,
        }
