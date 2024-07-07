from src.contexts.shared.domain import DomainEvent


class SerieCreatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.serie.created"


class SerieUpdatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.serie.updated"


class SerieDeletedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.serie.deleted"
