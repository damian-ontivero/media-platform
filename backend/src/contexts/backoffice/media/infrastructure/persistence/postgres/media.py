from sqlalchemy import Column, Integer, String
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresMedia(Base):
    __tablename__ = "media"

    id = Column(String(36), primary_key=True)
    type_ = Column(String(255))
    size = Column(Integer)
    duration = Column(Integer)
    resolution = Column(String(255))
    path = Column(String(255))

    def to_primitives(self) -> dict:
        return {
            "id": self.id,
            "type": self.type_,
            "size": self.size,
            "duration": self.duration,
            "resolution": self.resolution,
            "path": self.path,
        }
