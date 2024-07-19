from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.entity import Entity
from src.contexts.shared.domain.entity_id import EntityId


class AggregateRoot(Entity):
    """
    Base class for aggregate roots.

    Aggregate roots are entities that are the root of an aggregate.

    Aggregate roots are the only entities that can be accessed from outside the
    aggregate. They are responsible for enforcing the invariants of the aggregate
    and ensuring that the aggregate remains in a consistent state.

    Aggregate roots can record domain events that occurred during the execution
    of a use case. These domain events can be published to the event bus to notify
    other parts of the system that something has happened.
    """

    def __init__(self, id: EntityId) -> None:
        super().__init__(id)
        self._domain_events = []

    def pull_domain_events(self) -> list[DomainEvent]:
        """
        Pulls the domain events that were recorded by the aggregate root. The
        domain events are then cleared from the aggregate root.
        """
        domain_events = self._domain_events.copy()
        self._domain_events.clear()
        return domain_events

    def record(self, domain_event: DomainEvent) -> None:
        """
        Records a domain event that occurred during the execution of a use case.
        """
        if domain_event is None:
            raise RegisteredDomainEventError("Domain event cannot be None")
        self._domain_events.append(domain_event)


class RegisteredDomainEventError(Exception):
    pass
