from dataclasses import dataclass

from src.contexts.shared.domain.query_bus.query import Query


@dataclass(frozen=True)
class MediaCountQuery(Query):
    pass
