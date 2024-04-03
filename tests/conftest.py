import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.contexts.shared.infrastructure.persistence.sqlite import db

engine = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    import src.contexts.channel.channel.infrastructure.persistence.sqlite
    import src.contexts.channel.content.infrastructure.persistence.sqlite

    db.Base.metadata.create_all(bind=engine)
    yield
    db.Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def mock_channel_repository():
    from src.contexts.channel.channel.infrastructure.persistence.sqlite import (
        SqliteChannelRepository,
    )

    return SqliteChannelRepository(SessionLocal)


@pytest.fixture(scope="function")
def mock_content_repository():
    from src.contexts.channel.content.infrastructure.persistence.sqlite import (
        SqliteContentRepository,
    )

    return SqliteContentRepository(SessionLocal)
