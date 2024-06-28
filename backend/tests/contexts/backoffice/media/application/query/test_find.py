import faker
import pytest

from src.contexts.backoffice.media.application.query import MediaFindByIdQueryHandler
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


def test_media_finder__ok(mocker) -> None:
    media = MediaFactory()
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = media
    query = MediaFindByIdQuery(media.id.value)
    handler = MediaFindByIdQueryHandler(mock_media_repository)

    found_media = handler.handle(query)

    assert found_media == media


def test_media_finder__not_found(mocker) -> None:
    mock_media_repository = mocker.Mock()
    mock_media_repository.search.return_value = None
    query = MediaFindByIdQuery(faker.Faker().uuid4())
    handler = MediaFindByIdQueryHandler(mock_media_repository)

    with pytest.raises(Exception):
        handler.handle(query)
