from typing import Protocol

from .domain_event import DomainEvent


class EventBus(Protocol):
    def publish(self, domain_event: DomainEvent) -> None: ...
