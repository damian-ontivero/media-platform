import faker
import pytest
from src.contexts.backoffice.movies.application.commands.movie_create_command import MovieCreateCommand
from src.contexts.backoffice.movies.application.commands.movie_create_command_handler import MovieCreateCommandHandler
from src.contexts.backoffice.movies.application.services.movie_creator import MovieCreator
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


@pytest.mark.asyncio
async def test_movie_create__ok(mock_movie_repository, mock_query_bus, mock_event_bus) -> None:
    media = MediaFactory()
    mock_movie_repository.matching.return_value = None
    mock_query_bus.ask.return_value = media
    creator = MovieCreator(mock_movie_repository, mock_query_bus, mock_event_bus)
    handler = MovieCreateCommandHandler(creator)
    command = MovieCreateCommand(title=faker.Faker().name(), media_id=media.id.value)

    await handler.handle(command)

    mock_movie_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
