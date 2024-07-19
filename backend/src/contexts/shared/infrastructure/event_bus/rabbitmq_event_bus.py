import json

from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from src.contexts.shared.domain.event_bus.event_bus import EventBus
from src.contexts.shared.infrastructure.event_bus.rabbitmq_event_queue_formatter import RabbitMQEventQueueFormatter
from src.contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQEventBus(EventBus):
    def __init__(
        self, connection: RabbitMQConnection, exchange: str, queue_formatter: RabbitMQEventQueueFormatter
    ) -> None:
        self._connection = connection
        self._exchange = exchange
        self._queue_formatter = queue_formatter

    async def add_subscribers(self, subscribers: list[DomainEventSubscriber]) -> None:
        for subscriber in subscribers:
            queue_name = self._queue_formatter.format(subscriber)
            await self._connection.consume(queue_name)

    async def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            routing_key = event.type_
            message = json.dumps(event.to_primitives())
            await self._connection.publish(self._exchange, message, routing_key)
