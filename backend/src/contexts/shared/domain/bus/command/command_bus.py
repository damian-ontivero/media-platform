import abc

from .command import Command


class CommandBus(abc.ABC):
    """
    Interface for command buses.

    Command buses are responsible for dispatching commands to the appropriate
    command handler.
    """

    @abc.abstractmethod
    async def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class CommandHandlerNotFound(Exception):
    pass
