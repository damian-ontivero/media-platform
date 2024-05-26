import uuid


class EntityId:
    """
    Value object that represents the identity of an entity.

    Entity IDs are used to uniquely identify entities. They are immutable and
    cannot be changed once they are created.

    Entity IDs are compared by value. Two entity IDs are considered equal if
    they have the same value.
    """

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
        """
        Generates a new entity ID with a random UUID value.
        """
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
        return f"{self.__class__.__name__}(value={self._value!r})"
