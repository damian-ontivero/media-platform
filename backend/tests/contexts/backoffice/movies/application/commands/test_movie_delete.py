import faker
import pytest
from src.contexts.backoffice.movies.application.commands import MovieDeleteCommand, MovieDeleteCommandHandler
from src.contexts.backoffice.movies.application.services import MovieDeleter
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


@pytest.mark.asyncio
async def test_movie_delete__ok(mock_movie_repository, mock_event_bus) -> None:
    movie = MovieFactory()
    mock_movie_repository.search.return_value = movie
    deleter = MovieDeleter(mock_movie_repository, mock_event_bus)
    command = MovieDeleteCommand(movie.id.value)
    handler = MovieDeleteCommandHandler(deleter)

    await handler.handle(command)

    mock_movie_repository.delete.assert_called_once_with(movie.id.value)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_movie_delete__not_found(mock_movie_repository, mock_event_bus) -> None:
    mock_movie_repository.search.return_value = None
    deleter = MovieDeleter(mock_movie_repository, mock_event_bus)
    command = MovieDeleteCommand(faker.Faker().uuid4())
    handler = MovieDeleteCommandHandler(deleter)

    with pytest.raises(Exception):
        await handler.handle(command)