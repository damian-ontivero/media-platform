import pytest

from src.contexts.channel.content.application.content_finder import (
    ContentFinder,
)
from tests.utils.factories.channel.content import ContentFactory


def test_content_finder__ok(mock_content_repository) -> None:
    content = ContentFactory()
    finder = ContentFinder(mock_content_repository)

    found_content = finder.run(content.id.value)

    assert found_content.id == content.id
    assert found_content.files == content.files
    assert found_content.rating == content.rating
    assert found_content.metadata_ == content.metadata_


def test_content_finder__not_found(mock_content_repository) -> None:
    finder = ContentFinder(mock_content_repository)

    with pytest.raises(Exception):
        finder.run("not_found")
