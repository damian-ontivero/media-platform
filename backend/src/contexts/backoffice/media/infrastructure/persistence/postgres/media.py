from sqlalchemy import Column, Integer, String
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresMedia(Base):
    __tablename__ = "media"

    id = Column(String(36), primary_key=True)
    title = Column(String(255))
    size = Column(Integer)
    duration = Column(Integer)
    path = Column(String(255))

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "size": self.size, "duration": self.duration, "path": self.path}
