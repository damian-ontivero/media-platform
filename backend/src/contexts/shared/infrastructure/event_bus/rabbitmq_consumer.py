from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from src.contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQConsumer:
    def __init__(self, connection: RabbitMQConnection, subscriber: DomainEventSubscriber) -> None:
        self._connection = connection
        self._subscriber = subscriber

    async def on_message(self, message: str) -> None:
        print(f"Received message: {message}")
