from media_platform.backoffice.contexts.channel.channel.application.channel_creator import (
    ChannelCreator,
)


def test_channel_creator__ok(mock_channel_repository) -> None:
    creator = ChannelCreator(mock_channel_repository)

    creator.run(
        name="Test Channel",
        image={"path": "https://example.com/image.jpg"},
    )
