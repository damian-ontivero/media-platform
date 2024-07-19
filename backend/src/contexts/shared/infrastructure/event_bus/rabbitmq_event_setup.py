from src.contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from src.contexts.shared.infrastructure.event_bus.rabbitmq_event_configurer import RabbitMQEventConfigurer


class RabbitMQEventSetup:
    def __init__(self, configurer: RabbitMQEventConfigurer, subscribers: list[DomainEventSubscriber]) -> None:
        self._configurer = configurer
        self._subscribers = subscribers

    async def run(self) -> None:
        await self._configurer.configure(self._subscribers)
