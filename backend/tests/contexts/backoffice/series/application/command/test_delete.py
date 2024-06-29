import faker
import pytest
from src.contexts.backoffice.series.application.command import SerieDeleteCommand, SerieDeleteCommandHandler
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory


def test_serie_delete__ok(mocker) -> None:
    serie = SerieFactory()
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = serie
    mock_event_bus = mocker.Mock()
    command = SerieDeleteCommand(serie.id.value)
    handler = SerieDeleteCommandHandler(mock_serie_repository, mock_event_bus)

    await handler.handle(command)

    mock_serie_repository.delete.assert_called_once_with(serie.id.value)
    mock_event_bus.publish.assert_called_once()


def test_serie_delete__not_found(mocker) -> None:
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = None
    mock_event_bus = mocker.Mock()
    command = SerieDeleteCommand(faker.Faker().uuid4())
    handler = SerieDeleteCommandHandler(mock_serie_repository, mock_event_bus)

    with pytest.raises(Exception):
        await handler.handle(command)
