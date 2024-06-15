import faker
import pytest
from src.contexts.backoffice.movies.application.command import MovieDeleteCommand, MovieDeleteCommandHandler
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


def test_movie_eliminator__ok(mocker) -> None:
    movie = MovieFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = movie
    command = MovieDeleteCommand(movie.id.value)
    handler = MovieDeleteCommandHandler(mock_movie_repository)

    handler.handle(command)

    mock_movie_repository.delete.assert_called_once_with(movie.id.value)


def test_movie_eliminator__not_found(mocker) -> None:
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = None
    command = MovieDeleteCommand(faker.Faker().uuid4())
    handler = MovieDeleteCommandHandler(mock_movie_repository)

    with pytest.raises(Exception):
        handler.handle(command)
