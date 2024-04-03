import pytest

from src.contexts.channel.channel.application.channel_finder import (
    ChannelFinder,
)
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_finder__ok(mock_channel_repository) -> None:
    channel = ChannelFactory()
    finder = ChannelFinder(mock_channel_repository)

    found_channel = finder.run(channel.id.value)

    assert found_channel.id == channel.id
    assert found_channel.title == channel.title
    assert found_channel.languages == channel.languages
    assert found_channel.picture == channel.picture


def test_channel_finder__not_found(mock_channel_repository) -> None:
    finder = ChannelFinder(mock_channel_repository)

    with pytest.raises(Exception):
        finder.run("not_found")
