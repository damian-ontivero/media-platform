import faker
import pytest
from src.contexts.backoffice.series.application.command import SerieDeleteCommand, SerieDeleteCommandHandler
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


@pytest.mark.asyncio
async def test_serie_delete__ok(mocker) -> None:
    serie = SerieFactory()
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = serie
    mock_event_bus = mocker.AsyncMock()
    command = SerieDeleteCommand(serie.id.value)
    handler = SerieDeleteCommandHandler(mock_serie_repository, mock_event_bus)

    await handler.handle(command)

    mock_serie_repository.delete.assert_called_once_with(serie.id.value)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_serie_delete__not_found(mocker) -> None:
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = None
    mock_event_bus = mocker.AsyncMock()
    command = SerieDeleteCommand(faker.Faker().uuid4())
    handler = SerieDeleteCommandHandler(mock_serie_repository, mock_event_bus)

    with pytest.raises(Exception):
        await handler.handle(command)