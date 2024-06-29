import faker
import pytest
from src.contexts.backoffice.media.application.command import MediaUpdateCommand, MediaUpdateCommandHandler
from src.contexts.backoffice.media.domain import MediaDoesNotExist
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


def test_media_update__ok(mocker) -> None:
    media = MediaFactory()
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = media
    mock_media_repository.matching.return_value = None
    mock_event_bus = mocker.Mock()
    with open("backend/tests/data/video.mp4", "rb") as file:
        command = MediaUpdateCommand(
            id=media.id.value, title=faker.Faker().name(), file_name="video.mp4", file=file.read()
        )
        handler = MediaUpdateCommandHandler(mock_media_repository, mock_event_bus)

        await handler.handle(command)

        mock_media_repository.save.assert_called_once_with(media)
        mock_event_bus.publish.assert_called_once()


def test_media_update__not_found(mocker) -> None:
    media = MediaFactory()
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = None
    mock_event_bus = mocker.Mock()
    with open("backend/tests/data/video.mp4", "rb") as file:
        command = MediaUpdateCommand(
            id=media.id.value, title=faker.Faker().name(), file_name="video.mp4", file=file.read()
        )
        handler = MediaUpdateCommandHandler(mock_media_repository, mock_event_bus)

        with pytest.raises(MediaDoesNotExist):
            await handler.handle(command)
