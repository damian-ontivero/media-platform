from sqlalchemy import JSON, Column, String
from src.backoffice.contexts.shared.infrastructure.persistence.postgres.db import Base


class PostgresMovie(Base):
    __tablename__ = "movies"

    id = Column(String(36), primary_key=True)
    title = Column(String, index=True)
    links = Column(JSON)
