import pytest
from src.backoffice.contexts.channel.channel.application.channel_finder import ChannelFinder
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_finder__ok(mocker) -> None:
    channel = ChannelFactory()
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = channel
    finder = ChannelFinder(mock_channel_repository)

    found_channel = finder.run(channel.get_id())

    assert found_channel == channel


def test_channel_finder__not_found(mocker) -> None:
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = None
    finder = ChannelFinder(mock_channel_repository)

    with pytest.raises(Exception):
        finder.run("not_found")
