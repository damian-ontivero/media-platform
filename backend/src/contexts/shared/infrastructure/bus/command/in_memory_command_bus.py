from src.contexts.shared.domain.bus.command import Command, CommandBus, CommandHandler, RegisteredCommandError


class InMemoryCommandBus(CommandBus):
    def __init__(self, command_handlers: list[CommandHandler]) -> None:
        self._command_handler_map = {
            command_handler.subscribed_to(): command_handler for command_handler in command_handlers
        }

    def dispatch(self, command: Command) -> None:
        handler = self._command_handler_map.get(type(command))
        if handler is None:
            raise RegisteredCommandError(f"Command handler not found for {command.__class__.__name__}")
        handler.handle(command)
