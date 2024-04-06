import pytest
from media_platform.backoffice.contexts.channel.channel.application.channel_eliminator import (
    ChannelEliminator,
)
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_eliminator__ok(mock_channel_repository) -> None:
    channel = ChannelFactory()
    eliminator = ChannelEliminator(mock_channel_repository)

    eliminator.run(channel.id.value)


def test_channel_eliminator__not_found(mock_channel_repository) -> None:
    eliminator = ChannelEliminator(mock_channel_repository)

    with pytest.raises(Exception):
        eliminator.run("not_found")
