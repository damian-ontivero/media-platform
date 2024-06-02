from dataclasses import dataclass

from src.contexts.shared.domain.bus.query import Query


@dataclass(frozen=True)
class SerieFindByIdQuery(Query):
    id: str
