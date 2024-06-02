from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerie(Base):
    __tablename__ = "series"

    id = Column(String(36), primary_key=True)
    title = Column(String(255), index=True)
    seasons = relationship("PostgresSerieSeason")

    def to_primitives(self):
        return {"id": self.id, "title": self.title, "seasons": [season.to_primitives() for season in self.seasons]}
