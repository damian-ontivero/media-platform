import pytest
from src.contexts.backoffice.series.application.queries import (
    SerieSearchByCriteriaQuery,
    SerieSearchByCriteriaQueryHandler,
)
from src.contexts.backoffice.series.application.services import SerieSearcher
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


@pytest.mark.asyncio
async def test_searcher__ok(mock_serie_repository):
    series = SerieFactory.create_batch(10)
    mock_serie_repository.matching.return_value = series
    searcher = SerieSearcher(mock_serie_repository)
    query = SerieSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = SerieSearchByCriteriaQueryHandler(searcher)

    found_series = await handler.handle(query)

    assert len(found_series) == 10


@pytest.mark.asyncio
async def test_searcher__with_criteria__ok(mock_serie_repository):
    serie = SerieFactory(title="The Godfather")
    mock_serie_repository.matching.return_value = [serie]
    searcher = SerieSearcher(mock_serie_repository)
    query = SerieSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = SerieSearchByCriteriaQueryHandler(searcher)

    found_series = await handler.handle(query)

    assert found_series == [serie]
