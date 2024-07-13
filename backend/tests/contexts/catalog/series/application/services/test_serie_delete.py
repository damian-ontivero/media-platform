import faker
import pytest
from src.contexts.catalog.series.application.services import SerieDeleter
from tests.contexts.catalog.series.factory.serie_factory import SerieFactory


@pytest.mark.asyncio
async def test_serie_delete__ok(mock_serie_repository, mock_event_bus) -> None:
    serie = SerieFactory()
    mock_serie_repository.search.return_value = serie
    deleter = SerieDeleter(mock_serie_repository, mock_event_bus)

    await deleter.run(serie.id.value)

    mock_serie_repository.delete.assert_called_once_with(serie.id.value)
    mock_event_bus.publish.assert_called_once()