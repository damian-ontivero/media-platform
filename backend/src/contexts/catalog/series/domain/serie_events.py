from src.contexts.shared.domain import DomainEvent


class SerieCreatedDomainEvent(DomainEvent):
    EVENT_TYPE = "serie.created"


class SerieUpdatedDomainEvent(DomainEvent):
    EVENT_TYPE = "serie.updated"


class SerieDeletedDomainEvent(DomainEvent):
    EVENT_TYPE = "serie.deleted"
