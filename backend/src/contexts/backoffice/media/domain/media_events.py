from src.contexts.shared.domain import DomainEvent


class MediaCreatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.media.created"


class MediaUpdatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.media.updated"


class MediaDeletedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.media.deleted"
