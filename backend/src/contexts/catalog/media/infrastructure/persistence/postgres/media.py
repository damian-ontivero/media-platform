from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from src.contexts.catalog.media.domain.media import Media
from src.contexts.catalog.shared.infrastructure.persistence.postgres.db import Base


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
