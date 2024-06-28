import json
import os

import pika
from src.contexts.shared.domain import DomainEvent
from src.contexts.shared.domain.bus.event import EventBus


class RabbitMQEventBus(EventBus):

    _EXCHANGE = "catalog.domain_events"

    def __init__(self, url: str) -> None:
        if not url:
            raise RabbitMQEventBusError("URL is required")
        if not isinstance(url, str):
            raise RabbitMQEventBusError("URL must be a string")
        self._url = url

    def __enter__(self) -> "RabbitMQEventBus":
        self._connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._disconnect()

    @classmethod
    def create(cls, url: str = os.getenv("RABBITMQ_URL")) -> "RabbitMQEventBus":
        return cls(url)

    def _connect(self) -> None:
        self._connection = pika.BlockingConnection(pika.URLParameters(self._url))
        self._channel = self._connection.channel()

    def _disconnect(self) -> None:
        if self._connection and not self._connection.is_closed:
            self._connection.close()

    def publish(self, domain_events: list[DomainEvent]) -> None:
        with self:
            for domain_event in domain_events:
                self._channel.basic_publish(
                    exchange=self._EXCHANGE,
                    routing_key=domain_event.type_,
                    body=json.dumps(domain_event.to_primitives()),
                    properties=pika.BasicProperties(content_type="application/json"),
                )


class RabbitMQEventBusError(Exception):
    pass
