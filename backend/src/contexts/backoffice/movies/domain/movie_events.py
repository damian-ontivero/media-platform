from src.contexts.shared.domain import DomainEvent


class MovieCreated(DomainEvent):
    EVENT_TYPE = "movie_created"


class MovieUpdated(DomainEvent):
    EVENT_TYPE = "movie_updated"


class MovieDeleted(DomainEvent):
    EVENT_TYPE = "movie_deleted"
