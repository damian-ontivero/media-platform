import logging
import os

import httpx
from aio_pika import ExchangeType, connect_robust

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RABBITMQ_API = os.getenv("RABBITMQ_API")
RABBITMQ_URI = os.getenv("RABBITMQ_URI")


class RabbitMQManager:
    def __init__(self, uri: str, api: str) -> None:
        self._uri = uri
        self._api = api

    @classmethod
    def create(cls, uri: str = RABBITMQ_URI, api: str = RABBITMQ_API) -> "RabbitMQManager":
        return cls(uri, api)

    async def declare_vhost(self) -> None:
        async with httpx.AsyncClient() as client:
            vhost = self._uri.split("/")[-1]
            url = f"{self._api}/vhosts/{vhost}"
            response = await client.get(url)

            if response.status_code == 404:
                response = await client.put(url)
                if response.status_code == 201:
                    logger.info(f"Virtual host created: {vhost}")
                else:
                    raise Exception(f"Failed to create virtual host: {response.text}")
            elif response.status_code == 200:
                logger.info(f"Virtual host already exists: {vhost}")
            else:
                logger.error(f"Failed to check virtual host: {response.text}")
                raise Exception(f"Failed to check virtual host: {response.text}")

    async def declare_exchange(self, exchange_name: str) -> None:
        try:
            connection = await connect_robust(self._uri)
            async with connection:
                channel = await connection.channel()
                await channel.declare_exchange(exchange_name, ExchangeType.DIRECT, durable=True)
                logger.info(f"Exchange created: {exchange_name}")
        except Exception as e:
            logger.error(f"Failed to create exchange: {exchange_name}")
            logger.error(e)
            raise

    async def declare_queue(self, queue_name: str, exchange_name: str) -> None:
        try:
            connection = await connect_robust(self._uri)
            async with connection:
                channel = await connection.channel()
                queue = await channel.declare_queue(queue_name, durable=True)
                await queue.bind(exchange_name)
                logger.info(f"Queue created: {queue_name}")
        except Exception as e:
            logger.error(f"Failed to create queue: {queue_name}")
            logger.error(e)
            raise
