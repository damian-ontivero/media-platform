from abc import ABCMeta, abstractmethod

from .bus.event import DomainEvent
from .entity_id import EntityId


class Entity(metaclass=ABCMeta):

    class Created(DomainEvent):
        pass

    class Updated(DomainEvent):
        pass

    class Deleted(DomainEvent):
        pass

    @abstractmethod
    def __init__(self, id: EntityId, discarded: bool = False) -> None:
        self._id = id
        self._discarded = discarded

    @property
    def id(self) -> EntityId:
        return self._id

    @property
    def discarded(self) -> bool:
        return self._discarded

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return self._id == other._id

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._id)

    def _check_not_discarded(self) -> None:
        if self._discarded:
            raise DiscardedEntityError(
                f"Entity: {self._id.value!r} is discarded"
            )

    def discard(self) -> None:
        self._check_not_discarded()
        self._discarded = True


class DiscardedEntityError(Exception):
    pass
