from abc import ABC
from abc import abstractmethod

from src.contexts.shared.domain.command_bus.command import Command


class CommandHandler(ABC):
    """
    Interface for command handlers.

    Command handlers are responsible for handling commands that are dispatched
    by the command bus. They contain the business logic that is executed when
    a command is dispatched.

    Command handlers are subscribed to the commands they handle. When a command
    is dispatched, the command bus will find the appropriate command handler
    and call its handle method.
    """

    @staticmethod
    @abstractmethod
    def subscribed_to() -> Command:
        raise NotImplementedError

    @abstractmethod
    async def handle(self, command: Command) -> None:
        raise NotImplementedError
