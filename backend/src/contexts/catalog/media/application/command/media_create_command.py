from dataclasses import dataclass

from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class MediaCreateCommand(Command):
    title: str
    size: int
    duration: int
    file_path: str
