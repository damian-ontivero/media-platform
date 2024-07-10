import faker
import pytest
from src.contexts.backoffice.media.application.command import MediaDeleteCommand, MediaDeleteCommandHandler
from src.contexts.backoffice.media.application.services import MediaDeleter
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


@pytest.mark.asyncio
async def test_media_delete__ok(mock_media_repository, mock_event_bus) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    deleter = MediaDeleter(mock_media_repository, mock_event_bus)
    command = MediaDeleteCommand(media.id.value)
    handler = MediaDeleteCommandHandler(deleter)

    await handler.handle(command)

    mock_media_repository.delete.assert_called_once_with(media.id.value)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_media_delete__not_found(mock_media_repository, mock_event_bus) -> None:
    mock_media_repository.search.return_value = None
    deleter = MediaDeleter(mock_media_repository, mock_event_bus)
    command = MediaDeleteCommand(faker.Faker().uuid4())
    handler = MediaDeleteCommandHandler(deleter)

    with pytest.raises(Exception):
        await handler.handle(command)
