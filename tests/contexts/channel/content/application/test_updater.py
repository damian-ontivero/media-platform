import pytest

from src.contexts.channel.content.application.content_updater import (
    ContentUpdater,
)
from tests.utils.factories.channel.content import ContentFactory


def test_content_updater__ok(mock_content_repository) -> None:
    content = ContentFactory()
    updater = ContentUpdater(mock_content_repository)

    updater.run(
        id=content.id.value,
        files=[],
        rating=3.5,
        metadata_={},
        channel_id=content.channel_id.value,
    )


def test_content_updater__not_found(mock_content_repository) -> None:
    updater = ContentUpdater(mock_content_repository)

    with pytest.raises(Exception):
        updater.run(
            id="not_found",
            files=[],
            rating=3.5,
            metadata_=None,
        )
