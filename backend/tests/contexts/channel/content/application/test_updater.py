import pytest
from src.backoffice.contexts.channel.content.application.content_updater import ContentUpdater
from tests.utils.factories.channel.content import ContentFactory


def test_content_updater__ok(mocker) -> None:
    content = ContentFactory()
    mock_content_repository = mocker.Mock()
    mock_content_repository.search.return_value = content
    updater = ContentUpdater(mock_content_repository)

    updater.run(id=content.get_id(), files=[], rating=3.5, metadata_={}, channel_id=content.channel_id.value)

    mock_content_repository.update.assert_called_once_with(content)


def test_content_updater__not_found(mocker) -> None:
    mock_content_repository = mocker.Mock()
    mock_content_repository.search.return_value = None
    updater = ContentUpdater(mock_content_repository)

    with pytest.raises(Exception):
        updater.run(id="not_found", files=[], rating=3.5, metadata_=None)
