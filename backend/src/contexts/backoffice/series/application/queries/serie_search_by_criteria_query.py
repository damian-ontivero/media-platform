from dataclasses import dataclass

from src.contexts.shared.domain.criteria.filter import FilterDict
from src.contexts.shared.domain.criteria.sort import SortDict
from src.contexts.shared.domain.query_bus.query import Query


@dataclass(frozen=True)
class SerieSearchByCriteriaQuery(Query):
    filter: FilterDict | None
    sort: list[SortDict] | None
    page_size: int | None
    page_number: int | None
