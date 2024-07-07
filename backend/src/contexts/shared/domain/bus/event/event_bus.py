import abc

from src.contexts.shared.domain import DomainEvent


class EventBus(abc.ABC):
    """
    Interface for event buses.

    Event buses are responsible for publishing domain events that occurred
    during the execution of a use case. Other parts of the application can
    subscribe to these domain events and take action when they are published.
    """

    @abc.abstractmethod
    def publish(self, domain_events: list[DomainEvent]) -> None:
        raise NotImplementedError
