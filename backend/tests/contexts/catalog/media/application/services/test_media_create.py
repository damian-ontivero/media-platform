import faker
import pytest
from src.contexts.catalog.media.application.services.media_creator import MediaCreator


@pytest.mark.asyncio
async def test_media_create__ok(mock_media_repository, mock_event_bus) -> None:
    mock_media_repository.matching.return_value = None
    creator = MediaCreator(mock_media_repository, mock_event_bus)

    await creator.run(title=faker.Faker().name(), size=1000, duration=100, path="backend/tests/data/video.mp4")

    mock_media_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
