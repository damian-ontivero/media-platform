from src.contexts.shared.domain import DomainEvent


class MovieCreatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.movie.created"


class MovieUpdatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.movie.updated"


class MovieDeletedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.movie.deleted"
