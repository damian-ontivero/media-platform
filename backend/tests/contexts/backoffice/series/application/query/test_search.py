from src.contexts.backoffice.series.application.query import (
    SerieSearchByCriteriaQuery,
    SerieSearchByCriteriaQueryHandler,
)
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


def test_searcher__ok(mocker):
    series = SerieFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    mock_content_repository.matching.return_value = series
    query = SerieSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = SerieSearchByCriteriaQueryHandler(mock_content_repository)

    found_series = handler.handle(query)

    assert len(found_series) == 10


def test_searcher__with_criteria__ok(mocker):
    serie = SerieFactory(title="The Godfather")
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.matching.return_value = [serie]
    query = SerieSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = SerieSearchByCriteriaQueryHandler(mock_serie_repository)

    found_series = handler.handle(query)

    assert found_series == [serie]
