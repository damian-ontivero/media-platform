from dataclasses import dataclass

from src.contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class MovieUpdateCommand(Command):
    id: str
    title: str
    media_id: str
