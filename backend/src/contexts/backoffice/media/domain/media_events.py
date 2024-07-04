from src.contexts.shared.domain import DomainEvent


class MediaCreatedDomainEvent(DomainEvent):
    EVENT_TYPE = "media.created"


class MediaUpdatedDomainEvent(DomainEvent):
    EVENT_TYPE = "media.updated"


class MediaDeletedDomainEvent(DomainEvent):
    EVENT_TYPE = "media.deleted"
