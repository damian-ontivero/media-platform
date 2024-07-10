import faker
import pytest
from src.contexts.backoffice.media.application.query import MediaFindByIdQueryHandler
from src.contexts.backoffice.media.application.services import MediaFinder
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


@pytest.mark.asyncio
async def test_media_finder__ok(mock_media_repository) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    finder = MediaFinder(mock_media_repository)
    query = MediaFindByIdQuery(media.id.value)
    handler = MediaFindByIdQueryHandler(finder)

    found_media = await handler.handle(query)

    assert found_media == media


@pytest.mark.asyncio
async def test_media_finder__not_found(mock_media_repository) -> None:
    mock_media_repository.search.return_value = None
    finder = MediaFinder(mock_media_repository)
    query = MediaFindByIdQuery(faker.Faker().uuid4())
    handler = MediaFindByIdQueryHandler(finder)

    with pytest.raises(Exception):
        await handler.handle(query)
