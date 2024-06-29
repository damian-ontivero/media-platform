import faker
import pytest
from src.contexts.backoffice.series.application.query import SerieFindByIdQuery, SerieFindByIdQueryHandler
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


def test_serie_finder__ok(mocker) -> None:
    serie = SerieFactory()
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = serie
    query = SerieFindByIdQuery(serie.id.value)
    handler = SerieFindByIdQueryHandler(mock_serie_repository)

    found_serie = await handler.handle(query)

    assert found_serie == serie


def test_serie_finder__not_found(mocker) -> None:
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = None
    query = SerieFindByIdQuery(faker.Faker().uuid4())
    handler = SerieFindByIdQueryHandler(mock_serie_repository)

    with pytest.raises(Exception):
        await handler.handle(query)
