import asyncio

import dotenv

from src.apps.backoffice.api.v0.dependecy_injection import container
from src.contexts.shared.infrastructure.event_bus.rabbitmq_configurer import RabbitMQConfigurer

dotenv.load_dotenv("src/apps/backoffice/.env", override=True)


def run() -> None:
    configurer: RabbitMQConfigurer = container.find("RabbitMQConfigurer")

    asyncio.run(configurer.configure())
