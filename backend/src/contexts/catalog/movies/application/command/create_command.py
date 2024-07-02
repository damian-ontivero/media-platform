from dataclasses import dataclass

from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class MovieCreateCommand(Command):
    title: str
    duration: int
