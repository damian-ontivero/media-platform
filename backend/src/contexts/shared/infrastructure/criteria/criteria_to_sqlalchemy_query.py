from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Query

from src.contexts.shared.domain.criteria.condition import Condition
from src.contexts.shared.domain.criteria.criteria import Criteria
from src.contexts.shared.domain.criteria.filter import Filter
from src.contexts.shared.domain.criteria.sort import Sort


def equals_filter(m, k, v):
    return getattr(m, k) == v


def not_equals_filter(m, k, v):
    return getattr(m, k) != v


def contains_filter(m, k, v):
    return getattr(m, k).ilike(f"%{v}%")


def not_contains_filter(m, k, v):
    return getattr(m, k).notilike(f"%{v}%")


def is_any_of_filter(m, k, v):
    return getattr(m, k).in_(v.split(","))


def is_not_any_of_filter(m, k, v):
    return getattr(m, k).notin_(v.split(","))


def is_empty_filter(m, k, v):
    return getattr(m, k).is_(None)


def is_not_empty_filter(m, k, v):
    return getattr(m, k).isnot(None)


def starts_with_filter(m, k, v):
    return getattr(m, k).istartswith(f"{v}%")


def ends_with_filter(m, k, v):
    return getattr(m, k).iendswith(f"%{v}")


def gt_filter(m, k, v):
    return getattr(m, k) > v


def ge_filter(m, k, v):
    return getattr(m, k) >= v


def lt_filter(m, k, v):
    return getattr(m, k) < v


def le_filter(m, k, v):
    return getattr(m, k) <= v


FILTER_OPERATOR_MAPPER = {
    "EQUALS": equals_filter,
    "NOT_EQUALS": not_equals_filter,
    "CONTAINS": contains_filter,
    "NOT_CONTAINS": not_contains_filter,
    "IS_ANY_OF": is_any_of_filter,
    "IS_NOT_ANY_OF": is_not_any_of_filter,
    "IS_EMPTY": is_empty_filter,
    "IS_NOT_EMPTY": is_not_empty_filter,
    "STARTS_WITH": starts_with_filter,
    "ENDS_WITH": ends_with_filter,
    "GT": gt_filter,
    "GE": ge_filter,
    "LT": lt_filter,
    "LE": le_filter,
}


def criteria_to_sqlalchemy_query(query: Query, model: DeclarativeBase, criteria: Criteria) -> Query:
    """
    Convert a Criteria domain object to a SQLAlchemy query.
    """
    filters = []
    if criteria.filter is not None:
        filters.append(_process_filter(criteria.filter, model))
    if filters:
        query = query.filter(*filters)
    if criteria.sort is not None:
        for sort in criteria.sort:
            query = query.order_by(_process_sort(sort, model))
    if criteria.page_size is not None:
        query = query.limit(criteria.page_size.value)
    if criteria.page_size is not None and criteria.page_number is not None:
        query = query.offset((criteria.page_number.value - 1) * criteria.page_size.value)
    return query


def _process_filter(filter: Filter, model: DeclarativeBase):
    filters = []
    for condition in filter.conditions:
        if not hasattr(condition, "conjunction"):
            filters.append(_process_condition(condition, model))
        else:
            filters.append(_process_filter(condition, model))
    if filter.conjunction == "AND":
        return and_(*filters)
    return or_(*filters)


def _process_condition(condition: Condition, model: DeclarativeBase):
    return FILTER_OPERATOR_MAPPER[condition.operator](model, condition.field, condition.value)


def _process_sort(sort: Sort, model: DeclarativeBase):
    return getattr(model, sort.field).asc() if sort.direction == "ASC" else getattr(model, sort.field).desc()
