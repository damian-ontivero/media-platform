from sqlalchemy import Column, Integer, String

from src.contexts.backoffice.shared.infrastructure.persistence.postgres.db import Base
from src.contexts.catalog.media.domain.media import Media


class PostgresMedia(Base):
    __tablename__ = "media"

    id = Column(String(36), primary_key=True)
    title = Column(String, index=True)
    duration = Column(Integer)

    @classmethod
    def from_entity(cls, media: Media) -> "PostgresMedia":
        return cls(id=media.id.value, title=media.title, duration=media.duration)

    def update(self, media: Media) -> None:
        self.title = media.title
        self.duration = media.duration

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "duration": self.duration}
