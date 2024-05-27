from dataclasses import dataclass

from src.contexts.shared.domain.bus.query import Query


@dataclass(frozen=True)
class MediaSearchByCriteriaQuery(Query):
    filter: dict | None
    sort: list[dict] | None
    page_size: int | None
    page_number: int | None
