from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class RabbitMQEventConsumer:
    def __init__(self, subscribers: list[DomainEventSubscriber]) -> None:
        self._subscribers = subscribers

    async def on_message(self, message: str) -> None:
        pass
