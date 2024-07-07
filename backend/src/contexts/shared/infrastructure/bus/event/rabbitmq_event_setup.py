from src.contexts.shared.domain import DomainEventSubscriber
from src.contexts.shared.infrastructure.bus.event import RabbitMQEventConfigurer


class RabbitMQEventSetup:
    def __init__(self, configurer: RabbitMQEventConfigurer, subscribers: list[DomainEventSubscriber]) -> None:
        self._configurer = configurer
        self._subscribers = subscribers

    async def run(self) -> None:
        await self._configurer.configure(self._subscribers)
