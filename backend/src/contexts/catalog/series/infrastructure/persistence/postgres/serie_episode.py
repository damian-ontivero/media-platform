from sqlalchemy import Column, ForeignKey, Integer, String
from src.contexts.catalog.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerieEpisode(Base):
    __tablename__ = "serie_episodes"

    id = Column(String(36), primary_key=True)
    number = Column(Integer)
    title = Column(String(255))
    duration = Column(Integer)
    serie_season_id = Column(ForeignKey("serie_seasons.id"))

    def to_primitives(self) -> dict:
        return {"id": self.id, "number": self.number, "title": self.title, "duration": self.duration}
