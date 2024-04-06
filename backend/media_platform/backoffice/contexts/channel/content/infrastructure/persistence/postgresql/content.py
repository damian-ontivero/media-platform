import sqlalchemy as sa
from media_platform.backoffice.contexts.shared.infrastructure.persistence.postgresql import (
    db,
)


class PostgreSQLContentModel(db.Base):
    __tablename__ = "content"

    id = sa.Column(sa.String(36), primary_key=True, index=True)
    files = sa.Column(sa.JSON)
    rating = sa.Column(sa.Float)
    metadata_ = sa.Column(sa.JSON)
    channel_id = sa.Column(sa.String(36), sa.ForeignKey("channel.id"))
