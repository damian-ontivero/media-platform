import abc

from .domain_event import DomainEvent


class DomainEventSubscriber(abc.ABC):
    """
    Interface for domain event subscribers.

    Domain event subscribers are subscribed to domain events and are notified
    when a domain event is published.
    """

    @abc.abstractmethod
    def subscribed_to(self) -> list[DomainEvent]:
        raise NotImplementedError

    @abc.abstractmethod
    async def on(self, event: DomainEvent) -> None:
        raise NotImplementedError
