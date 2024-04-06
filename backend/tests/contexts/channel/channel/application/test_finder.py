import pytest
from media_platform.backoffice.contexts.channel.channel.application.channel_finder import (
    ChannelFinder,
)
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_finder__ok(mock_channel_repository) -> None:
    channel = ChannelFactory()
    finder = ChannelFinder(mock_channel_repository)

    found_channel = finder.run(channel.id.value)

    assert found_channel.id == channel.id
    assert found_channel.name == channel.name
    assert found_channel.image == channel.image


def test_channel_finder__not_found(mock_channel_repository) -> None:
    finder = ChannelFinder(mock_channel_repository)

    with pytest.raises(Exception):
        finder.run("not_found")
