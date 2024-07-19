from dataclasses import dataclass

from src.contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class MediaDeleteCommand(Command):
    id: str
