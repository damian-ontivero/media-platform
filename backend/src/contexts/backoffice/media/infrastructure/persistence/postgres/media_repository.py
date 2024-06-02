from sqlalchemy.orm import Session
from src.contexts.backoffice.media.domain import Media, MediaRepository
from src.contexts.shared.infrastructure.criteria import criteria_to_sqlalchemy_query

from .media import PostgresMedia


class PostgresMediaRepository(MediaRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def search_all(self) -> list[Media]:
        with self._session() as session:
            query = session.query(PostgresMedia)
            return [Media.from_primitives(**media_db.to_primitives()) for media_db in query.all()]

    def search(self, id: str) -> Media | None:
        with self._session() as session:
            media_db = session.get(PostgresMedia, id)
            if media_db is None:
                return None
            return Media.from_primitives(**media_db.to_primitives())

    def matching(self, criteria) -> list[Media]:
        with self._session() as session:
            query = session.query(PostgresMedia)
            query = criteria_to_sqlalchemy_query(query, PostgresMedia, criteria)
            return [Media.from_primitives(**media_db.to_primitives()) for media_db in query.all()]

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgresMedia).count()

    def save(self, media: Media) -> None:
        with self._session() as session:
            media_db = PostgresMedia(**media.to_primitives())
            session.merge(media_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            media_db = session.get(PostgresMedia, id)
            session.delete(media_db)
            session.commit()
