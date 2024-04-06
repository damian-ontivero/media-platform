import pytest
from media_platform.backoffice.contexts.shared.infrastructure.persistence.postgresql import (
    db,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    import media_platform.backoffice.contexts.channel.channel.infrastructure.persistence.postgresql
    import media_platform.backoffice.contexts.channel.content.infrastructure.persistence.postgresql

    db.Base.metadata.create_all(bind=engine)
    yield
    db.Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def mock_channel_repository():
    from media_platform.backoffice.contexts.channel.channel.infrastructure.persistence.postgresql import (
        PostgreSQLChannelRepository,
    )

    return PostgreSQLChannelRepository(SessionLocal)


@pytest.fixture(scope="function")
def mock_content_repository():
    from media_platform.backoffice.contexts.channel.content.infrastructure.persistence.postgresql import (
        PostgreSQLContentRepository,
    )

    return PostgreSQLContentRepository(SessionLocal)
