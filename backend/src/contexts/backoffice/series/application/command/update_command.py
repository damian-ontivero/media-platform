from dataclasses import dataclass

from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class SerieUpdateCommand(Command):
    id: str
    title: str
    seasons: list
