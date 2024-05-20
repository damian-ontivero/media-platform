import uuid


class EntityId:

    __slots__ = ("_value",)

    def __new__(cls, value: str) -> "EntityId":
        instance = super().__new__(cls)
        instance._value = value
        return instance

    @property
    def value(self) -> str:
        return str(self._value)

    @classmethod
    def generate(cls) -> "EntityId":
        return cls(str(uuid.uuid4()))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntityId):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return ("{c}(value={value!r})").format(c=self.__class__.__name__, value=self._value)
