from src.contexts.backoffice.movies.application.movie_searcher import MovieSearcher
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


def test_searcher__ok(mocker):
    MovieFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    searcher = MovieSearcher(mock_content_repository)

    found_channels = searcher.run()

    assert len(found_channels) == 10


def test_searcher__with_criteria__ok(mocker):
    MovieFactory.create_batch(10)
    mock_movie_repository = mocker.Mock()
    searcher = MovieSearcher(mock_movie_repository)
    criteria = {
        "filter": {"conjunction": "AND", "conditions": [{"field": "rating", "operator": "GT", "value": "3"}]},
        "sort": [{"field": "rating", "direction": "ASC"}],
        "page_size": None,
        "page_number": None,
    }

    found_channels = searcher.run(criteria)

    assert all(found_channel.rating > 3 for found_channel in found_channels)


def test_searcher__with_criteria__ko(mocker):
    MovieFactory.create_batch(10)
    mock_movie_repository = mocker.Mock()
    searcher = MovieSearcher(mock_movie_repository)
    criteria = {
        "filter": {"conjunction": "AND", "conditions": [{"field": "rating", "operator": "GT", "value": "3"}]},
        "sort": [{"field": "rating", "direction": "ASC"}],
        "page_size": None,
        "page_number": None,
    }

    found_channels = searcher.run(criteria)

    assert not all(found_channel.rating <= 3 for found_channel in found_channels)
