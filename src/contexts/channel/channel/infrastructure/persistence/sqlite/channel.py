import sqlalchemy as sa

from src.contexts.shared.infrastructure.persistence.sqlite import db


class SqliteChannelModel(db.Base):
    __tablename__ = "channel"

    id = sa.Column(sa.String(36), primary_key=True, index=True)
    title = sa.Column(sa.String)
    languages = sa.Column(sa.JSON)
    picture = sa.Column(sa.JSON)
