import faker
import pytest
from src.contexts.backoffice.movies.application.command import MovieUpdateCommand, MovieUpdateCommandHandler
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


def test_movie_updater__ok(mocker) -> None:
    movie = MovieFactory()
    media = MediaFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = movie
    mock_query_bus = mocker.Mock()
    mock_query_bus.ask.return_value = media
    command = MovieUpdateCommand(id=movie.id.value, title=faker.Faker().name(), media_id=media.id.value)
    handler = MovieUpdateCommandHandler(mock_movie_repository, mock_query_bus)

    handler.handle(command)

    mock_movie_repository.save.assert_called_once_with(movie)


def test_movie_updater__not_found(mocker) -> None:
    media = MediaFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = None
    mock_query_bus = mocker.Mock()
    mock_query_bus.ask.return_value = media
    command = MovieUpdateCommand(id=faker.Faker().uuid4(), title=faker.Faker().name(), media_id=media.id.value)
    handler = MovieUpdateCommandHandler(mock_movie_repository, mock_query_bus)

    with pytest.raises(Exception):
        handler.handle(command)
