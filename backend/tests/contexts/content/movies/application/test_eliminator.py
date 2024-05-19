import pytest
from src.backoffice.contexts.content.movies.application.movie_eliminator import MovieEliminator
from tests.utils.factories.channel.content import ContentFactory


def test_movie_eliminator__ok(mocker) -> None:
    movie = ContentFactory()
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
