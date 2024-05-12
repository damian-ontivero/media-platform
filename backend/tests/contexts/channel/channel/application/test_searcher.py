from src.backoffice.contexts.channel.channel.application.channel_searcher import ChannelSearcher
from tests.utils.factories.channel.channel import ChannelFactory


def test_searcher__ok(mocker):
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = ChannelFactory.create_batch(10)
    searcher = ChannelSearcher(mock_channel_repository)

    found_channels = searcher.run()

    assert len(found_channels) == 10
