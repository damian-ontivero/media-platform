from abc import ABCMeta, abstractmethod

from .domain_event import DomainEvent


class EventBus(metaclass=ABCMeta):

    @abstractmethod
    def publish(self, domain_event: DomainEvent) -> None:
        raise NotImplementedError
