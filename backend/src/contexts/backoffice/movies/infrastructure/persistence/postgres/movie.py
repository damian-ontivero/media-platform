from sqlalchemy import Column, ForeignKey, String
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresMovie(Base):
    __tablename__ = "movies"

    id = Column(String(36), primary_key=True)
    title = Column(String, index=True)
    media_id = Column(ForeignKey("media.id"))

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "media_id": self.media_id}
