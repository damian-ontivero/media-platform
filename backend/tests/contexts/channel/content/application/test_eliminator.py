import pytest
from src.backoffice.contexts.channel.content.application.content_eliminator import ContentEliminator
from tests.utils.factories.channel.content import ContentFactory


def test_content_eliminator__ok(mocker) -> None:
    content = ContentFactory()
    mock_content_repository = mocker.Mock()
    mock_content_repository.search.return_value = content
    eliminator = ContentEliminator(mock_content_repository)

    eliminator.run(content.get_id())

    mock_content_repository.delete.assert_called_once_with(content.get_id())


def test_content_eliminator__not_found(mocker) -> None:
    mock_content_repository = mocker.Mock()
    mock_content_repository.search.return_value = None
    eliminator = ContentEliminator(mock_content_repository)

    with pytest.raises(Exception):
        eliminator.run("not_found")
