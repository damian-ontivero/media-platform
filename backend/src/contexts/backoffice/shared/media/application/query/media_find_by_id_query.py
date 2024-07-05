from dataclasses import dataclass

from src.contexts.shared.domain.bus.query import Query


@dataclass(frozen=True)
class MediaFindByIdQuery(Query):
    id: str
