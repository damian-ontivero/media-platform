import pytest
from src.backoffice.contexts.channel.content.application.content_finder import ContentFinder
from tests.utils.factories.channel.content import ContentFactory


def test_content_finder__ok(mocker) -> None:
    content = ContentFactory()
    mock_content_repository = mocker.Mock()
    mock_content_repository.search.return_value = content
    finder = ContentFinder(mock_content_repository)

    found_content = finder.run(content.get_id())

    assert found_content == content


def test_content_finder__not_found(mocker) -> None:
    mock_content_repository = mocker.Mock()
    mock_content_repository.search.return_value = None
    finder = ContentFinder(mock_content_repository)

    with pytest.raises(Exception):
        finder.run("not_found")
