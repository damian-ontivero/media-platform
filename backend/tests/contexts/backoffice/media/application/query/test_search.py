import pytest
from src.contexts.backoffice.media.application.query import (
    MediaSearchByCriteriaQuery,
    MediaSearchByCriteriaQueryHandler,
)
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


@pytest.mark.asyncio
async def test_searcher__ok(mocker):
    media = MediaFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    mock_content_repository.matching.return_value = media
    query = MediaSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = MediaSearchByCriteriaQueryHandler(mock_content_repository)

    found_media = await handler.handle(query)

    assert len(found_media) == 10


@pytest.mark.asyncio
async def test_searcher__with_criteria__ok(mocker):
    media = MediaFactory(title="The Godfather")
    mock_media_repository = mocker.Mock()
    mock_media_repository.matching.return_value = [media]
    query = MediaSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = MediaSearchByCriteriaQueryHandler(mock_media_repository)

    found_media = await handler.handle(query)

    assert found_media == [media]
