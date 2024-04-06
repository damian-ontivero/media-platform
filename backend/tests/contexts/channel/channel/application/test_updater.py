import pytest
from media_platform.backoffice.contexts.channel.channel.application.channel_updater import (
    ChannelUpdater,
)
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_updater__ok(mock_channel_repository) -> None:
    channel = ChannelFactory()
    updater = ChannelUpdater(mock_channel_repository)

    updater.run(
        id=channel.id.value,
        name="Test Channel",
        image={"path": "https://example.com/image.jpg"},
    )


def test_channel_updater__not_found(mock_channel_repository) -> None:
    updater = ChannelUpdater(mock_channel_repository)

    with pytest.raises(Exception):
        updater.run(
            id="not_found",
            name="Test Channel",
            image={"path": "https://example.com/image.jpg"},
        )
