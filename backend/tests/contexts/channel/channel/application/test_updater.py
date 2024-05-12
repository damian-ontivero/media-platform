import pytest
from src.backoffice.contexts.channel.channel.application.channel_updater import ChannelUpdater
from tests.utils.factories.channel.channel import ChannelFactory


def test_channel_updater__ok(mocker) -> None:
    channel = ChannelFactory()
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = channel
    updater = ChannelUpdater(mock_channel_repository)

    updater.run(id=channel.get_id(), name="Test Channel", image={"path": "https://example.com/image.jpg"})

    mock_channel_repository.save.assert_called_once()


def test_channel_updater__not_found(mocker) -> None:
    mock_channel_repository = mocker.Mock()
    mock_channel_repository.search.return_value = None
    updater = ChannelUpdater(mock_channel_repository)

    with pytest.raises(Exception):
        updater.run(id="not_found", name="Test Channel", image={"path": "https://example.com/image.jpg"})
