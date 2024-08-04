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

    EVENT_NAME: str

    __slots__ = ("_id", "_type", "_occurred_on", "_data")

    def __init__(self, id: str, type_: str, occurred_on: str, data: dict) -> "DomainEvent":
        self._id = id
        self._type = type_
        self._occurred_on = occurred_on
        self._data = data

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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DomainEvent):
            return NotImplemented
        return self._id == other._id

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._id)

    def __repr__(self) -> str:
        return "{c}(id={id!r}, type_={type_!r}, occurred_on={occurred_on!r}, data={data!r})".format(
            c=self.__class__.__name__, id=self._id, type_=self._type, occurred_on=self._occurred_on, data=self._data
        )

    @classmethod
    def create(cls, data: dict) -> "DomainEvent":
        return cls(str(uuid.uuid4()), cls.EVENT_NAME, datetime.datetime.now(datetime.UTC).isoformat(), data)

    def to_primitives(self) -> dict:
        return {"id": self._id, "type": self._type, "occurred_on": self._occurred_on, "data": self._data}
