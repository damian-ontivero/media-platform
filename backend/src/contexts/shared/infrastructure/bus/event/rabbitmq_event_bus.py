import json
import os

import pika

from src.contexts.shared.domain import DomainEvent
from src.contexts.shared.domain.bus.event import EventBus


class RabbitMQEventBus(EventBus):
    def __init__(self, domain: str, subdomain: str, uri_scheme: str, host: str, username: str, password: str) -> None:
        self._domain = domain
        self._subdomain = subdomain
        self._url = f"{uri_scheme}://{username}:{password}@{host}?heartbeat=1800"

    def _connect(self) -> None:
        self._connection = pika.BlockingConnection(pika.URLParameters(self._url))
        self._channel = self._connection.channel()

    def _disconnect(self) -> None:
        if self._connection and not self._connection.is_closed:
            self._connection.close()

    def __enter__(self) -> "RabbitMQEventBus":
        self._connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._disconnect()

    def publish(self, domain_events: list[DomainEvent]) -> None:
        with self:
            for domain_event in domain_events:
                self._channel.basic_publish(
                    exchange=f"{self._domain}.{self._subdomain}.domain_events",
                    routing_key=domain_event.type,
                    body=json.dumps(domain_event.to_primitives()),
                    properties=pika.BasicProperties(content_type="application/json"),
                )


rabbitmq_event_bus = RabbitMQEventBus(
    "buildplatf",
    "backoffice",
    os.getenv("RABBITMQ_AMQP_URI_SCHEME"),
    os.getenv("RABBITMQ_HOST"),
    os.getenv("RABBITMQ_USERNAME"),
    os.getenv("RABBITMQ_PASSWORD"),
)
