import faker

from src.contexts.backoffice.media.application.command import MediaCreateCommand, MediaCreateCommandHandler


def test_media_create__ok(mocker) -> None:
    mock_media_repository = mocker.Mock()
    mock_media_repository.matching.return_value = None
    mock_event_bus = mocker.Mock()
    with open("backend/tests/data/video.mp4", "rb") as file:
        command = MediaCreateCommand(title=faker.Faker().name(), file_name="video.mp4", file=file.read())
        handler = MediaCreateCommandHandler(mock_media_repository, mock_event_bus)

        handler.handle(command)

        mock_media_repository.save.assert_called_once()
