from src.contexts.channel.channel.application.channel_searcher import (
    ChannelSearcher,
)
from tests.utils.factories.channel.channel import ChannelFactory


def test_searcher__ok(mock_channel_repository):
    ChannelFactory.create_batch(10)
    searcher = ChannelSearcher(mock_channel_repository)

    found_channels = searcher.run()

    assert len(found_channels) == 10
