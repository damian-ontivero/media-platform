from abc import ABCMeta, abstractmethod

from .entity_id import EntityId


class Entity(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, id: EntityId) -> None:
        self._id = id

    @property
    def id(self) -> EntityId:
        return self._id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return self._id == other._id

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._id)


class DiscardedEntityError(Exception):
    pass
