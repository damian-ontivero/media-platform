import faker
import pytest
from src.contexts.catalog.movies.application.services import MovieCreator
from tests.contexts.catalog.media.factory.media_factory import MediaFactory


@pytest.mark.asyncio
async def test_movie_create__ok(mock_movie_repository, mock_query_bus, mock_event_bus) -> None:
    media = MediaFactory()
    mock_movie_repository.matching.return_value = None
    mock_query_bus.ask.return_value = media
    creator = MovieCreator(mock_movie_repository, mock_query_bus, mock_event_bus)

    await creator.run(title=faker.Faker().name(), media_id=media.id.value)

    mock_movie_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
