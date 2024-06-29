import json
import logging
import os

from aio_pika import Message, connect_robust
from src.contexts.shared.domain import DomainEvent
from src.contexts.shared.domain.bus.event import EventBus

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


RABBITMQ_URI = os.getenv("RABBITMQ_URI")


class RabbitMQEventBus(EventBus):

    _EXCHANGE = "backoffice.domain_events"

    def __init__(self, uri: str) -> None:
        if not uri:
            raise RabbitMQEventBusError("URI is required")
        if not isinstance(uri, str):
            raise RabbitMQEventBusError("URI must be a string")
        self._uri = uri

    @classmethod
    def create(cls, uri: str = RABBITMQ_URI) -> "RabbitMQEventBus":
        return cls(uri)

    async def publish(self, domain_events: list[DomainEvent]) -> None:
        try:
            connection = await connect_robust(self._uri)
            async with connection:
                channel = await connection.channel()
                exchange = await channel.get_exchange(self._EXCHANGE)
                for domain_event in domain_events:
                    await exchange.publish(
                        Message(body=json.dumps(domain_event.to_primitives()).encode()), routing_key=domain_event.type_
                    )
        except Exception as e:
            logger.error(f"Failed to publish domain events: {e}")
            raise RabbitMQEventBusError("Failed to publish domain events")


class RabbitMQEventBusError(Exception):
    pass
