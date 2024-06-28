from src.contexts.shared.domain import DomainEvent


class SerieCreated(DomainEvent):
    EVENT_TYPE = "serie_created"


class SerieUpdated(DomainEvent):
    EVENT_TYPE = "serie_updated"


class SerieDeleted(DomainEvent):
    EVENT_TYPE = "serie_deleted"
