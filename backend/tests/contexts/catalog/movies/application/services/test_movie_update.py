import faker
import pytest

from src.contexts.catalog.movies.application.services.movie_updater import MovieUpdater

from tests.contexts.catalog.media.factory.media_factory import MediaFactory
from tests.contexts.catalog.movies.factory.movie_factory import MovieFactory


@pytest.mark.asyncio
async def test_movie_update__ok(mock_movie_repository, mock_query_bus, mock_event_bus) -> None:
    movie = MovieFactory()
    media = MediaFactory()
    mock_movie_repository.search.return_value = movie
    mock_movie_repository.matching.return_value = None
    mock_query_bus.ask.return_value = media
    updater = MovieUpdater(mock_movie_repository, mock_query_bus, mock_event_bus)

    await updater.run(id=movie.id.value, title=faker.Faker().name(), media_id=media.id.value)

    mock_movie_repository.save.assert_called_once_with(movie)
    mock_event_bus.publish.assert_called_once()
