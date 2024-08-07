from aio_pika import IncomingMessage

from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from src.contexts.shared.infrastructure.logger.logger import Logger
from src.contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQConsumer:
    def __init__(self, connection: RabbitMQConnection, subscriber: DomainEventSubscriber, logger: Logger) -> None:
        self._connection = connection
        self._subscriber = subscriber
        self._logger = logger

    async def on_message(self, message: IncomingMessage) -> None:
        event = self._subscriber.decode(message.body)
        await self._subscriber.on(event)
