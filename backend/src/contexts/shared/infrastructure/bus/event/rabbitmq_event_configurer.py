from src.contexts.shared.domain import DomainEventSubscriber
from src.contexts.shared.infrastructure.rabbitmq import RabbitMQConnection

from .rabbitmq_event_exchange_formatter import RabbitMQEventExchangeFormatter
from .rabbitmq_event_queue_formatter import RabbitMQEventQueueFormatter


class RabbitMQEventConfigurer:
    def __init__(
        self,
        connection: RabbitMQConnection,
        exchange_formatter: RabbitMQEventExchangeFormatter,
        queue_formatter: RabbitMQEventQueueFormatter,
    ) -> None:
        self._connection = connection
        self._exchange_formatter = exchange_formatter
        self._queue_formatter = queue_formatter

    async def configure(self, subscribers: list[DomainEventSubscriber]) -> None:
        await self._declare_exchange(self._exchange_formatter.format())
        for subscriber in subscribers:
            await self._declare_queue(subscriber)

    async def _declare_exchange(self, exchange_name: str) -> None:
        await self._connection.declare_exchange(exchange_name, "direct")

    async def _declare_queue(self, subscriber: DomainEventSubscriber) -> None:
        routing_keys = [event.EVENT_NAME for event in subscriber.subscribed_to()]
        queue_name = self._queue_formatter.format(subscriber.__class__.__name__)
        await self._connection.declare_queue(queue_name, routing_keys)
