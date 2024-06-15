import faker
import pytest
from src.contexts.backoffice.media.application.command import MediaDeleteCommand, MediaDeleteCommandHandler
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


def test_media_eliminator__ok(mocker) -> None:
    media = MediaFactory()
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = media
    command = MediaDeleteCommand(media.id.value)
    handler = MediaDeleteCommandHandler(mock_media_repository)

    handler.handle(command)

    mock_media_repository.delete.assert_called_once_with(media.id.value)


def test_media_eliminator__not_found(mocker) -> None:
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = None
    command = MediaDeleteCommand(faker.Faker().uuid4())
    handler = MediaDeleteCommandHandler(mock_media_repository)

    with pytest.raises(Exception):
        handler.handle(command)
