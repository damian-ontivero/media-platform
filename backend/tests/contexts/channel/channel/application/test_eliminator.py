import pytest
from src.backoffice.contexts.channel.channel.application.channel_eliminator import ChannelEliminator
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_eliminator__ok(mocker) -> None:
    channel = ChannelFactory()
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = channel
    eliminator = ChannelEliminator(mock_channel_repository)

    eliminator.run(channel.get_id())

    mock_channel_repository.delete.assert_called_once_with(channel.get_id())


def test_channel_eliminator__not_found(mocker) -> None:
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = None
    eliminator = ChannelEliminator(mock_channel_repository)

    with pytest.raises(Exception):
        eliminator.run("not_found")
