from .bus.event import DomainEvent
from .entity import Entity
from .entity_id import EntityId


class AggregateRoot(Entity):

    def __init__(self, id: EntityId, discarded: bool = False) -> None:
        super().__init__(id, discarded)
        self._domain_events = []

    @property
    def domain_events(self) -> list[DomainEvent]:
        return self._domain_events

    def _register_domain_event(self, domain_event: DomainEvent) -> None:
        if domain_event is None:
            raise RegisteredDomainEventError("Domain event is None")
        self._domain_events.append(domain_event)

    def clear_domain_events(self) -> None:
        self._domain_events.clear()


class RegisteredDomainEventError(Exception):
    pass
