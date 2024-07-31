import asyncio

import dotenv

from src.apps.catalog.api.v0.dependecy_injection import container
from src.contexts.shared.infrastructure.event_bus.rabbitmq_configurer import RabbitMQConfigurer

dotenv.load_dotenv("src/apps/catalog/.env", override=True)


def run() -> None:
    configurer: RabbitMQConfigurer = container.find("RabbitMQConfigurer")

    asyncio.run(configurer.configure())
