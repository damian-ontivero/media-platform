from sqlalchemy.orm import Session
from src.backoffice.contexts.channel.content.domain import Content, ContentRepository
from src.backoffice.contexts.shared.domain.criteria import Criteria
from src.backoffice.contexts.shared.infrastructure.criteria import criteria_to_sqlalchemy_query

from .content import PostgreSQLContentModel


class PostgreSQLContentRepository(ContentRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def search_all(self) -> list[Content]:
        with self._session() as session:
            query = session.query(PostgreSQLContentModel)
            content_db = query.all()
            return [
                Content.from_primitives(
                    content_db.id, content_db.files, content_db.rating, content_db.metadata_, content_db.channel_id
                )
                for content_db in content_db
            ]

    def search(self, id: str) -> Content | None:
        with self._session() as session:
            content_db = session.get(PostgreSQLContentModel, id)
            if content_db is not None:
                return Content.from_primitives(
                    content_db.id, content_db.files, content_db.rating, content_db.metadata_, content_db.channel_id
                )

    def matching(self, criteria: Criteria) -> list[Content]:
        with self._session() as session:
            query = session.query(PostgreSQLContentModel)
            query = criteria_to_sqlalchemy_query(query, PostgreSQLContentModel, criteria)
            content_db = query.all()
            return [
                Content.from_primitives(
                    content_db.id, content_db.files, content_db.rating, content_db.metadata_, content_db.channel_id
                )
                for content_db in content_db
            ]

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgreSQLContentModel).count()

    def save(self, content: Content) -> None:
        with self._session() as session:
            content_db = session.get(PostgreSQLContentModel, content.get_id())
            content_db = PostgreSQLContentModel(**content.to_primitives())
            session.add(content_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            content_db = session.get(PostgreSQLContentModel, id)
            session.delete(content_db)
            session.commit()