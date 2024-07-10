import faker
import pytest
from src.contexts.backoffice.media.application.command import MediaCreateCommand, MediaCreateCommandHandler
from src.contexts.backoffice.media.application.services import MediaCreator


@pytest.mark.asyncio
async def test_media_create__ok(mock_media_repository, mock_event_bus) -> None:
    mock_media_repository.matching.return_value = None
    creator = MediaCreator(mock_media_repository, mock_event_bus)
    with open("tests/data/video.mp4", "rb") as file:
        command = MediaCreateCommand(title=faker.Faker().name(), file_name="video.mp4", file=file.read())
        handler = MediaCreateCommandHandler(creator)

        await handler.handle(command)

        mock_media_repository.save.assert_called_once()
        mock_event_bus.publish.assert_called_once()
