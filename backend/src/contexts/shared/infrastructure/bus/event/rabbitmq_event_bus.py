import json

from src.contexts.shared.domain import DomainEvent
from src.contexts.shared.domain.bus.event import EventBus
from src.contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQEventBus(EventBus):
    def __init__(self, connection: RabbitMQConnection, exchange_formatter) -> None:
        self._connection = connection
        self._exchange_formatter = exchange_formatter

    async def publish(self, events: list[DomainEvent]) -> None:
        exchange = self._exchange_formatter.format()
        for event in events:
            message = json.dumps(event.to_primitives())
            await self._connection.publish(exchange, message, event.type_)
