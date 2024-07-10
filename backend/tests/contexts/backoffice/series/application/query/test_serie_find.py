import faker
import pytest
from src.contexts.backoffice.series.application.query import SerieFindByIdQuery, SerieFindByIdQueryHandler
from src.contexts.backoffice.series.application.services import SerieFinder
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


@pytest.mark.asyncio
async def test_serie_finder__ok(mock_serie_repository) -> None:
    serie = SerieFactory()
    mock_serie_repository.search.return_value = serie
    finder = SerieFinder(mock_serie_repository)
    query = SerieFindByIdQuery(serie.id.value)
    handler = SerieFindByIdQueryHandler(finder)

    found_serie = await handler.handle(query)

    assert found_serie == serie


@pytest.mark.asyncio
async def test_serie_finder__not_found(mock_serie_repository) -> None:
    mock_serie_repository.search.return_value = None
    finder = SerieFinder(mock_serie_repository)
    query = SerieFindByIdQuery(faker.Faker().uuid4())
    handler = SerieFindByIdQueryHandler(finder)

    with pytest.raises(Exception):
        await handler.handle(query)
