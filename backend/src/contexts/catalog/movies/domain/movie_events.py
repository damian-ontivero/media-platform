from src.contexts.shared.domain import DomainEvent


class MovieCreatedDomainEvent(DomainEvent):
    EVENT_TYPE = "movie.created"


class MovieUpdatedDomainEvent(DomainEvent):
    EVENT_TYPE = "movie.updated"


class MovieDeletedDomainEvent(DomainEvent):
    EVENT_TYPE = "movie.deleted"
