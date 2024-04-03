from src.contexts.channel.channel.application.channel_creator import (
    ChannelCreator,
)


def test_channel_creator__ok(mock_channel_repository) -> None:
    creator = ChannelCreator(mock_channel_repository)

    creator.run(
        title="Test Channel",
        languages=["en", "es"],
        picture={"path": "https://example.com/picture.jpg"},
    )
