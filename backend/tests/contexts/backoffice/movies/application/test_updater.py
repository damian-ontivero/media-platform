import pytest
from src.contexts.backoffice.movies.application.movie_updater import MovieUpdater
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


def test_movie_updater__ok(mocker) -> None:
    movie = MovieFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = movie
    updater = MovieUpdater(mock_movie_repository)

    updater.run(id=movie.id, files=[], rating=3.5, metadata_={}, channel_id=movie.channel_id.value)

    mock_movie_repository.update.assert_called_once_with(movie)


def test_movie_updater__not_found(mocker) -> None:
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = None
    updater = MovieUpdater(mock_movie_repository)

    with pytest.raises(Exception):
        updater.run(id="not_found", files=[], rating=3.5, metadata_=None)
