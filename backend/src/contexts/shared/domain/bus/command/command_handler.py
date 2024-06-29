from abc import ABC, abstractmethod

from .command import Command


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

    @abstractmethod
    def subscribed_to(self) -> Command:
        raise NotImplementedError

    @abstractmethod
    async def handle(self, command: Command) -> None:
        raise NotImplementedError
