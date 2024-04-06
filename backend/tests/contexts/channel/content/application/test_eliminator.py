import pytest
from media_platform.backoffice.contexts.channel.content.application.content_eliminator import (
    ContentEliminator,
)
from tests.utils.factories.channel.content import ContentFactory


def test_content_eliminator__ok(mock_content_repository) -> None:
    content = ContentFactory()
    eliminator = ContentEliminator(mock_content_repository)

    eliminator.run(content.id.value)


def test_content_eliminator__not_found(mock_content_repository) -> None:
    eliminator = ContentEliminator(mock_content_repository)

    with pytest.raises(Exception):
        eliminator.run("not_found")
