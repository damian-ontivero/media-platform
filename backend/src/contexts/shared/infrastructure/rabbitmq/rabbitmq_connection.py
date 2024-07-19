from aio_pika import ExchangeType, Message, connect_robust
from src.contexts.shared.infrastructure.rabbitmq.rabbitmq_config import RabbitMQConfig


class RabbitMQConnection:
    def __init__(self, config: RabbitMQConfig) -> None:
        self._config = config

    async def declare_exchange(self, exchange_name: str, exchange_type: str) -> None:
        connection = await connect_robust(self._config._uri)
        async with connection:
            channel = await connection.channel()
            await channel.declare_exchange(exchange_name, ExchangeType(exchange_type), durable=True)

    async def declare_queue(self, queue_name: str, routing_keys: list[str]) -> None:
        connection = await connect_robust(self._config._uri)
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue(queue_name, durable=True)
            for routing_key in routing_keys:
                exchange_name = routing_key.split(".")[0] + ".domain_events"
                await queue.bind(exchange_name, routing_key)

    async def publish(self, exchange_name: str, message: str, routing_key: str) -> None:
        connection = await connect_robust(self._config._uri)
        async with connection:
            channel = await connection.channel()
            exchange = await channel.get_exchange(exchange_name)
            await exchange.publish(Message(body=message.encode(), content_type="application/json"), routing_key)

    async def consume(self, queue_name: str, callback) -> None:
        connection = await connect_robust(self._config._uri)
        async with connection:
            channel = await connection.channel()
            queue = await channel.get_queue(queue_name)
            await queue.consume(callback)
