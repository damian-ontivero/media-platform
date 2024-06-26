from dataclasses import dataclass

from src.contexts.backoffice.series.domain import SerieSeasonDict
from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class SerieCreateCommand(Command):
    title: str
    seasons: list[SerieSeasonDict]
