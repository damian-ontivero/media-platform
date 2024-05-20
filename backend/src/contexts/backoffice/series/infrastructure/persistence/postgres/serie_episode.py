from sqlalchemy import Column, ForeignKey, String
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerieEpisode(Base):
    __tablename__ = "serie_episodes"

    id = Column(String(36), primary_key=True)
    number = Column(String(255))
    title = Column(String(255))
    media_id = Column(ForeignKey("media.id"))
    serie_season_id = Column(ForeignKey("serie_seasons.id"))

    def to_primitives(self) -> dict:
        return {"id": self.id, "number": self.number, "title": self.title, "media_id": self.media_id}
