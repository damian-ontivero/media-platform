from src.backoffice.contexts.channel.content.application.content_searcher import ContentSearcher
from tests.utils.factories.channel.content import ContentFactory


def test_searcher__ok(mocker):
    ContentFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    searcher = ContentSearcher(mock_content_repository)

    found_channels = searcher.run()

    assert len(found_channels) == 10


def test_searcher__with_criteria__ok(mocker):
    ContentFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    searcher = ContentSearcher(mock_content_repository)
    criteria = {
        "filter": {"conjunction": "AND", "conditions": [{"field": "rating", "operator": "GT", "value": "3"}]},
        "sort": [{"field": "rating", "direction": "ASC"}],
        "page_size": None,
        "page_number": None,
    }

    found_channels = searcher.run(criteria)

    assert all(found_channel.rating > 3 for found_channel in found_channels)


def test_searcher__with_criteria__ko(mocker):
    ContentFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    searcher = ContentSearcher(mock_content_repository)
    criteria = {
        "filter": {"conjunction": "AND", "conditions": [{"field": "rating", "operator": "GT", "value": "3"}]},
        "sort": [{"field": "rating", "direction": "ASC"}],
        "page_size": None,
        "page_number": None,
    }

    found_channels = searcher.run(criteria)

    assert not all(found_channel.rating <= 3 for found_channel in found_channels)
