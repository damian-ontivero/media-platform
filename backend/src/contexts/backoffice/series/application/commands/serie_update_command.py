from dataclasses import dataclass

from src.contexts.backoffice.series.domain.serie_season import SerieSeasonDict
from src.contexts.shared.domain.command_bus.command import Command


@dataclass(frozen=True)
class SerieUpdateCommand(Command):
    id: str
    title: str
    seasons: list[SerieSeasonDict]
