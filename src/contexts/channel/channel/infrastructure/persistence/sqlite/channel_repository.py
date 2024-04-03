from sqlalchemy.orm import Session

from src.contexts.channel.channel.domain import Channel, ChannelRepository
from src.contexts.shared.domain.criteria import Criteria
from src.contexts.shared.infrastructure.criteria import (
    criteria_to_sqlalchemy_query,
)

from .channel import SqliteChannelModel


class SqliteChannelRepository(ChannelRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    def search_all(self) -> list[Channel]:
        with self._session() as session:
            query = session.query(SqliteChannelModel)
            channels_db = query.all()

            return [
                Channel.from_primitives(
                    channel_db.id,
                    channel_db.title,
                    channel_db.languages,
                    channel_db.picture,
                )
                for channel_db in channels_db
            ]

    def search(self, id: str) -> Channel | None:
        with self._session() as session:
            channel_db = session.get(SqliteChannelModel, id)

            if channel_db is not None:
                return Channel.from_primitives(
                    channel_db.id,
                    channel_db.title,
                    channel_db.languages,
                    channel_db.picture,
                )

    def matching(self, criteria: Criteria) -> list[Channel]:
        with self._session() as session:
            query = session.query(SqliteChannelModel)
            query = criteria_to_sqlalchemy_query(
                query, SqliteChannelModel, criteria
            )
            channels_db = query.all()

            return [
                Channel.from_primitives(
                    channel_db.id,
                    channel_db.title,
                    channel_db.languages,
                    channel_db.picture,
                )
                for channel_db in channels_db
            ]

    def count(self) -> int:
        with self._session() as session:
            return session.query(SqliteChannelModel).count()

    def save(self, channel: Channel) -> None:
        with self._session() as session:
            channel_db = session.get(SqliteChannelModel, channel.id.value)

            if channel_db is not None:
                channel_db.title = channel.title
                channel_db.languages = channel.languages
                channel_db.picture = (
                    channel.picture.__dict__ if channel.picture else None
                )

            else:
                channel_db = SqliteChannelModel(**channel.to_primitives())
                session.add(channel_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            channel_db = session.get(SqliteChannelModel, id)
            session.delete(channel_db)
            session.commit()
