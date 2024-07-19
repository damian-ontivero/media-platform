import asyncio

import dotenv
from src.apps.catalog.api.v0.dependecy_injection import container
from src.contexts.shared.infrastructure.event_bus.rabbitmq_event_setup import RabbitMQEventSetup

dotenv.load_dotenv("src/apps/catalog/.env", override=True)


def run_rabbitmq_setup() -> None:
    setup: RabbitMQEventSetup = container.get("RabbitMQEventSetup")

    asyncio.run(setup.run())


if __name__ == "__main__":
    run_rabbitmq_setup()
