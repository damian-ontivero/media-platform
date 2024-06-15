import faker
import pytest
from src.contexts.backoffice.media.application.command import MediaUpdateCommand, MediaUpdateCommandHandler
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


def test_media_updater__ok(mocker) -> None:
    media = MediaFactory()
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = media
    with open("backend/tests/data/video.mp4", "rb") as file:
        command = MediaUpdateCommand(
            id=media.id.value, title=faker.Faker().name(), file_name="video.mp4", file=file.read()
        )
        handler = MediaUpdateCommandHandler(mock_media_repository)

        handler.handle(command)

        mock_media_repository.save.assert_called_once_with(media)


def test_media_updater__not_found(mocker) -> None:
    media = MediaFactory()
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = None
    with open("backend/tests/data/video.mp4", "rb") as file:
        command = MediaUpdateCommand(
            id=media.id.value, title=faker.Faker().name(), file_name="video.mp4", file=file.read()
        )
        handler = MediaUpdateCommandHandler(mock_media_repository)

        with pytest.raises(Exception):
            handler.handle(command)
