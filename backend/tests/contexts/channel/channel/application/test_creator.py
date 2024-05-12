from src.backoffice.contexts.channel.channel.application.channel_creator import ChannelCreator


def test_channel_creator__ok(mocker) -> None:
    mock_channel_repository = mocker.Mock()
    creator = ChannelCreator(mock_channel_repository)

    creator.run(name="Test Channel", image={"path": "https://example.com/image.jpg"})

    mock_channel_repository.save.assert_called_once()
