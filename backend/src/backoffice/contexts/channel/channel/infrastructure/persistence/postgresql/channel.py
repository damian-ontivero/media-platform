import sqlalchemy as sa
from src.backoffice.contexts.shared.infrastructure.persistence.postgresql import db


class PostgreSQLChannelModel(db.Base):
    __tablename__ = "channel"

    id = sa.Column(sa.String(36), primary_key=True, index=True)
    name = sa.Column(sa.String)
    image = sa.Column(sa.JSON)
