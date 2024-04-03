from src.contexts.channel.content.application.content_creator import (
    ContentCreator,
)


def test_content_creator__ok(mock_content_repository) -> None:
    creator = ContentCreator(mock_content_repository)

    with open("tests/utils/data/file_example_MP4_1920_18MG.mp4", "rb") as f:
        data = f.read()

    creator.run(
        files=[
            {
                "name": "image.jpg",
                "data": data,
                "media_type": "image/jpeg",
            }
        ],
        rating=4.5,
        metadata_={"title": "Title", "description": "Description"},
        channel_id="channel_id",
    )