import datetime
import uuid


class DomainEvent:
    """
    Value object that represents a domain event.

    Domain events are used to communicate changes in the domain model. They are
    immutable and cannot be changed once they are created.

    Domain events are compared by value. Two domain events are considered equal
    if they have the same value.
    """

    __slots__ = ("_id", "_type", "_occurred_on", "_data")

    def __new__(cls, id: str, type_: str, occurred_on: str, data: dict) -> "DomainEvent":
        instance = super().__new__(cls)
        instance._id = id
        instance._type = type_
        instance._occurred_on = occurred_on
        instance._data = data
        return instance

    @property
    def id(self) -> str:
        return str(self._id)

    @property
    def type_(self) -> str:
        return str(self._type)

    @property
    def occurred_on(self) -> str:
        return str(self._occurred_on)

    @property
    def data(self) -> dict:
        return dict(self._data)

    @classmethod
    def create(cls, type_: str, data: dict) -> "DomainEvent":
        return cls(str(uuid.uuid4()), type_, datetime.datetime.now(datetime.UTC).isoformat(), data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DomainEvent):
            return NotImplemented
        return (
            self._id == other._id
            and self._type == other._type
            and self._occurred_on == other._occurred_on
            and self._data == other._data
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._id, self._type, self._occurred_on, self._data))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(id={self._id!r}, type_={self._type!r}, occurred_on={self._occurred_on!r}, data={self._data!r})"
        )
