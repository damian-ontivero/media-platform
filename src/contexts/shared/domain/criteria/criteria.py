from .filter import Filter
from .sort import Sort


class Criteria:

    __slots__ = (
        "_filter",
        "_sort",
        "_page_size",
        "_page_number",
    )

    def __init__(
        self,
        filter: Filter | None,
        sort: list[Sort] | None,
        page_size: int | None,
        page_number: int | None,
    ):
        if filter is not None:
            if not isinstance(filter, Filter):
                raise TypeError("Filter must be a Filter")
        if sort is not None:
            if not isinstance(sort, list):
                raise TypeError("Sort must be a list")
            if not all(isinstance(s, Sort) for s in sort):
                raise TypeError("All elements of sort must be a Sort")
        if page_size is not None:
            if not isinstance(page_size, int):
                raise TypeError("Page size must be an integer")
            if page_size < 1:
                raise ValueError("Page size must be greater than 0")
        if page_number is not None:
            if not isinstance(page_number, int):
                raise TypeError("Page number must be an integer")
            if page_number < 1:
                raise ValueError("Page number must be greater than 0")
        self._filter = filter
        self._sort = sort
        self._page_size = page_size
        self._page_number = page_number

    @property
    def filter(self) -> Filter | None:
        return self._filter

    @property
    def sort(self) -> list[Sort] | None:
        return self._sort

    @property
    def page_size(self) -> int | None:
        return self._page_size

    @property
    def page_number(self) -> int | None:
        return self._page_number

    @classmethod
    def from_primitives(
        cls,
        filter: dict | None,
        sort: list[dict] | None,
        page_size: int | None,
        page_number: int | None,
    ) -> "Criteria":
        return cls(
            filter=Filter.from_primitives(**filter) if filter else None,
            sort=[Sort.from_primitives(**s) for s in sort] if sort else None,
            page_size=page_size,
            page_number=page_number,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Criteria):
            return NotImplemented
        return (
            self._filter == other._filter
            and self._sort == other._sort
            and self._page_size == other._page_size
            and self._page_number == other._page_number
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                self._filter,
                self._sort,
                self._page_size,
                self._page_number,
            )
        )

    def __repr__(self) -> str:
        return (
            "{c}(filter={filter!r}, sort={sort!r}, page_size={page_size!r}, "
            "page_number={page_number!r})"
        ).format(
            c=self.__class__.__name__,
            filter=self._filter,
            sort=self._sort,
            page_size=self._page_size,
            page_number=self._page_number,
        )
