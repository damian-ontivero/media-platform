from dataclasses import dataclass

from src.contexts.shared.domain.bus.query import Query
from src.contexts.shared.domain.criteria import FilterDict, SortDict


@dataclass(frozen=True)
class MovieSearchByCriteriaQuery(Query):
    filter: FilterDict | None
    sort: list[SortDict] | None
    page_size: int | None
    page_number: int | None
