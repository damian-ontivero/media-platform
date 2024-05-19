import pytest
from src.backoffice.contexts.content.movies.application.movie_finder import MovieFinder
from tests.utils.factories.channel.content import ContentFactory


def test_movie_finder__ok(mocker) -> None:
    movie = ContentFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = movie
    finder = MovieFinder(mock_movie_repository)

    found_movie = finder.run(movie.id)

    assert found_movie == movie


def test_movie_finder__not_found(mocker) -> None:
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = None
    finder = MovieFinder(mock_movie_repository)

    with pytest.raises(Exception):
        finder.run("not_found")
