import logging

import httpx
from aio_pika import ExchangeType, connect_robust

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def declare_vhost(api: str, uri: str):
    async with httpx.AsyncClient() as client:
        vhost = uri.split("/")[-1]
        url = f"{api}/vhosts/{vhost}"
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
            raise Exception(f"Error checking virtual host : {response.text}")


async def declare_exchange(uri: str, exchange: str):
    try:
        connection = await connect_robust(uri)
        async with connection:
            channel = await connection.channel()
            await channel.declare_exchange(exchange, ExchangeType.DIRECT, durable=True)
            logger.info(f"Exchange created: {exchange}")
    except Exception as e:
        logger.error(f"Failed to create exchange: {exchange}")
        logger.error(e)
        raise
