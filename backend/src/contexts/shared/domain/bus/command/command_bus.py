from abc import ABC, abstractmethod

from .command import Command


class CommandBus(ABC):
    """
    Interface for command buses.

    Command buses are responsible for dispatching commands to the appropriate
    command handler.
    """

    @abstractmethod
    async def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class CommandHandlerNotFound(Exception):
    pass
