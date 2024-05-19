import pytest
from src.backoffice.contexts.content.movies.application.movie_updater import MovieUpdater
from tests.utils.factories.channel.content import ContentFactory


def test_movie_updater__ok(mocker) -> None:
    movie = ContentFactory()
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
