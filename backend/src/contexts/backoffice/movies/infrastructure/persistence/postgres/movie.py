from sqlalchemy import Column, ForeignKey, String
from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresMovie(Base):
    __tablename__ = "movies"

    id = Column(String(36), primary_key=True)
    title = Column(String, index=True)
    media_id = Column(ForeignKey("media.id"))

    @classmethod
    def from_entity(cls, movie: Movie) -> "PostgresMovie":
        return cls(id=movie.id.value, title=movie.title, media_id=movie.media_id.value)

    def update(self, movie: Movie) -> None:
        self.title = movie.title
        self.media_id = movie.media_id.value

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "media_id": self.media_id}
