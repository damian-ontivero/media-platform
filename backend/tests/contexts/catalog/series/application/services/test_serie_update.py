import faker
import pytest

from src.contexts.catalog.series.application.services.serie_updater import SerieUpdater
from tests.contexts.catalog.media.factory.media_factory import MediaFactory
from tests.contexts.catalog.series.factory.serie_factory import SerieFactory
from tests.contexts.catalog.series.factory.serie_season_factory import SerieSeasonFactory


@pytest.mark.asyncio
async def test_serie_update__ok(mock_serie_repository, mock_query_bus, mock_event_bus) -> None:
    serie = SerieFactory()
    seasons = SerieSeasonFactory.create_batch(3)
    media = MediaFactory()
    mock_serie_repository.search.return_value = serie
    mock_serie_repository.matching.return_value = None
    updater = SerieUpdater(mock_serie_repository, mock_query_bus, mock_event_bus)
    id = serie.id.value
    title = faker.Faker().name()
    seasons = [
        {
            "number": season.number,
            "episodes": [
                {"number": episode.number, "title": episode.title, "media_id": media.id.value}
                for episode in season.episodes
            ],
        }
        for season in seasons
    ]

    await updater.run(id=id, title=title, seasons=seasons)

    mock_serie_repository.save.assert_called_once_with(serie)
    mock_event_bus.publish.assert_called_once()
