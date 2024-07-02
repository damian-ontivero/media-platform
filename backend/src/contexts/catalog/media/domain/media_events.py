from src.contexts.shared.domain import DomainEvent


class MediaCreated(DomainEvent):
    EVENT_TYPE = "media_created"


class MediaUpdated(DomainEvent):
    EVENT_TYPE = "media_updated"


class MediaDeleted(DomainEvent):
    EVENT_TYPE = "media_deleted"
