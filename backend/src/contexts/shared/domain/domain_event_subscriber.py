from abc import ABC, abstractmethod

from .domain_event import DomainEvent


class DomainEventSubscriber(ABC):
    """
    Interface for domain event subscribers.

    Domain event subscribers are subscribed to domain events and are notified
    when a domain event is published.
    """

    @staticmethod
    @abstractmethod
    def subscribed_to() -> list[DomainEvent]:
        raise NotImplementedError

    @abstractmethod
    async def on(self, event: DomainEvent) -> None:
        raise NotImplementedError
