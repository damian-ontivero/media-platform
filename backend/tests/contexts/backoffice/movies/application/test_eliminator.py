import pytest
from src.contexts.backoffice.movies.application.movie_eliminator import MovieEliminator
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


def test_movie_eliminator__ok(mocker) -> None:
    movie = MovieFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = movie
    eliminator = MovieEliminator(mock_movie_repository)

    eliminator.run(movie.id)

    mock_movie_repository.delete.assert_called_once_with(movie.id)


def test_movie_eliminator__not_found(mocker) -> None:
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = None
    eliminator = MovieEliminator(mock_movie_repository)

    with pytest.raises(Exception):
        eliminator.run("not_found")
