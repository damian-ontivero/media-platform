import pytest

from src.contexts.channel.channel.application.channel_updater import (
    ChannelUpdater,
)
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_updater__ok(mock_channel_repository) -> None:
    channel = ChannelFactory()
    updater = ChannelUpdater(mock_channel_repository)

    updater.run(
        id=channel.id.value,
        title="Test Channel",
        languages=["en", "es"],
        picture={"path": "https://example.com/picture.jpg"},
    )


def test_channel_updater__not_found(mock_channel_repository) -> None:
    updater = ChannelUpdater(mock_channel_repository)

    with pytest.raises(Exception):
        updater.run(
            id="not_found",
            title="Test Channel",
            languages=["en", "es"],
            picture={"path": "https://example.com/picture.jpg"},
        )
