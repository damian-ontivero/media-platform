from media_platform.backoffice.contexts.channel.channel.domain import (
    Channel,
    ChannelRepository,
)
from media_platform.backoffice.contexts.shared.domain.criteria import Criteria
from media_platform.backoffice.contexts.shared.infrastructure.criteria import (
    criteria_to_sqlalchemy_query,
)
from sqlalchemy.orm import Session

from .channel import PostgreSQLChannelModel


class PostgreSQLChannelRepository(ChannelRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    def search_all(self) -> list[Channel]:
        with self._session() as session:
            query = session.query(PostgreSQLChannelModel)
            channels_db = query.all()

            return [
                Channel.from_primitives(
                    channel_db.id,
                    channel_db.name,
                    channel_db.image,
                )
                for channel_db in channels_db
            ]

    def search(self, id: str) -> Channel | None:
        with self._session() as session:
            channel_db = session.get(PostgreSQLChannelModel, id)

            if channel_db is not None:
                return Channel.from_primitives(
                    channel_db.id,
                    channel_db.name,
                    channel_db.image,
                )

    def matching(self, criteria: Criteria) -> list[Channel]:
        with self._session() as session:
            query = session.query(PostgreSQLChannelModel)
            query = criteria_to_sqlalchemy_query(
                query, PostgreSQLChannelModel, criteria
            )
            channels_db = query.all()

            return [
                Channel.from_primitives(
                    channel_db.id,
                    channel_db.name,
                    channel_db.image,
                )
                for channel_db in channels_db
            ]

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgreSQLChannelModel).count()

    def save(self, channel: Channel) -> None:
        with self._session() as session:
            channel_db = session.get(PostgreSQLChannelModel, channel.id.value)

            if channel_db is not None:
                channel_db.name = channel.name
                channel_db.image = (
                    channel.image.__dict__ if channel.image else None
                )

            else:
                channel_db = PostgreSQLChannelModel(**channel.to_primitives())
                session.add(channel_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            channel_db = session.get(PostgreSQLChannelModel, id)
            session.delete(channel_db)
            session.commit()
