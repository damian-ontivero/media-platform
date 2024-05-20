from src.contexts.shared.domain import AggregateRoot, EntityId


class Media(AggregateRoot):
    def __init__(self, id: EntityId, type_: str, size: int, duration: int, resolution: str, path: str) -> None:
        self._id = id
        self._type = type_
        self._size = size
        self._duration = duration
        self._resolution = resolution
        self._path = path

    @property
    def type_(self) -> str:
        return self._type

    @property
    def size(self) -> int:
        return self._size

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def resolution(self) -> str:
        return self._resolution

    @property
    def path(self) -> str:
        return self._path

    @classmethod
    def create(cls, type_: str, size: int, duration: int, resolution: str, path: str) -> "Media":
        media = cls(EntityId.generate(), type_, size, duration, resolution, path)
        return media

    @classmethod
    def from_primitives(cls, id: str, type_: str, size: int, duration: int, resolution: str, path: str) -> "Media":
        return cls(EntityId(id), type_, size, duration, resolution, path)

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "type": self._type,
            "size": self._size,
            "duration": self._duration,
            "resolution": self._resolution,
            "path": self._path,
        }
