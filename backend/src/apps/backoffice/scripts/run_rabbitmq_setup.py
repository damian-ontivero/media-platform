import asyncio

import dotenv
from src.apps.backoffice.api.v0.dependecy_injection import container
from src.contexts.shared.infrastructure.bus.event.rabbitmq_event_setup import RabbitMQEventSetup

dotenv.load_dotenv("src/apps/backoffice/.env", override=True)


def run_rabbitmq_setup() -> None:
    setup: RabbitMQEventSetup = container.get("RabbitMQEventSetup")

    asyncio.run(setup.run())


if __name__ == "__main__":
    run_rabbitmq_setup()
