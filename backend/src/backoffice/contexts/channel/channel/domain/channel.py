from src.backoffice.contexts.shared.domain import AggregateRoot, EntityId, Image


class Channel(AggregateRoot):
    def __init__(self, id: EntityId, name: str, image: Image) -> None:
        super().__init__(id)
        self._name = name
        self._image = image

    @classmethod
    def create(cls, name: str, image: dict) -> "Channel":
        return cls(EntityId.generate(), name, Image(image["path"]) if image else None)

    @classmethod
    def from_primitives(cls, id: str, name: str, image: dict) -> "Channel":
        return cls(EntityId(id), name, Image(image["path"]) if image else None)

    def update(self, name: str, image: dict) -> None:
        if not name == self._name:
            self._name = name
        if not image == self._image:
            self._image = Image(image["path"]) if image else None

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "name": self._name, "image": self._image.__dict__ if self._image else None}

    def __repr__(self) -> str:
        return ("{c}(id={id!r}, name={name!r}, image={image!r})").format(
            c=self.__class__.__name__, id=self._id, name=self._name, image=self._image
        )
