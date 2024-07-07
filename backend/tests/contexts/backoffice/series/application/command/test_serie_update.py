import faker
import pytest
from src.contexts.backoffice.series.application.command import SerieUpdateCommand, SerieUpdateCommandHandler
from src.contexts.backoffice.series.domain import SerieDoesNotExist
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory
from tests.contexts.backoffice.series.factory.serie_season_factory import SerieSeasonFactory


@pytest.mark.asyncio
async def test_serie_update__ok(mocker) -> None:
    serie = SerieFactory()
    seasons = SerieSeasonFactory.create_batch(3)
    media = MediaFactory()
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = serie
    mock_serie_repository.matching.return_value = None
    mock_query_bus = mocker.AsyncMock()
    mock_event_bus = mocker.AsyncMock()
    handler = SerieUpdateCommandHandler(mock_serie_repository, mock_query_bus, mock_event_bus)
    command = SerieUpdateCommand(
        id=serie.id.value,
        title=faker.Faker().name(),
        seasons=[
            {
                "number": season.number,
                "episodes": [
                    {"number": episode.number, "title": episode.title, "media_id": media.id.value}
                    for episode in season.episodes
                ],
            }
            for season in seasons
        ],
    )

    await handler.handle(command)

    mock_serie_repository.save.assert_called_once_with(serie)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_serie_update__not_found(mocker) -> None:
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.search.return_value = None
    mock_query_bus = mocker.AsyncMock()
    mock_event_bus = mocker.AsyncMock()
    handler = SerieUpdateCommandHandler(mock_serie_repository, mock_query_bus, mock_event_bus)
    command = SerieUpdateCommand(id=faker.Faker().uuid4(), title=faker.Faker().name(), seasons=[])

    with pytest.raises(SerieDoesNotExist):
        await handler.handle(command)
