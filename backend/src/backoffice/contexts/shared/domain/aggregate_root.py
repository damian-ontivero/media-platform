from .bus.event import DomainEvent
from .entity import Entity
from .entity_id import EntityId


class AggregateRoot(Entity):
    def __init__(self, id: EntityId) -> None:
        super().__init__(id)
        self._domain_events = []

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self._domain_events.copy()
        self._domain_events.clear()
        return domain_events

    def record(self, domain_event: DomainEvent) -> None:
        if domain_event is None:
            raise RegisteredDomainEventError("Domain event is None")
        self._domain_events.append(domain_event)


class RegisteredDomainEventError(Exception):
    pass
