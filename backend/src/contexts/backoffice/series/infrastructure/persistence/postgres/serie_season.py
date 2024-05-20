from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerieSeason(Base):
    __tablename__ = "serie_seasons"

    id = Column(String(36), primary_key=True)
    number = Column(String(255))
    serie_id = Column(ForeignKey("series.id"))
    episodes = relationship("PostgresSerieEpisode", back_populates="serie_season")

    def to_primitives(self) -> dict:
        return {
            "id": self.id,
            "number": self.number,
            "episodes": [episode.to_primitives() for episode in self.episodes],
        }
