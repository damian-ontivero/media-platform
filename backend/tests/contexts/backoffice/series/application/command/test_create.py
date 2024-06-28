import faker

from src.contexts.backoffice.series.application.command import SerieCreateCommand, SerieCreateCommandHandler
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory
from tests.contexts.backoffice.series.factory.serie_season_factory import SerieSeasonFactory


def test_serie_create__ok(mocker) -> None:
    media = MediaFactory()
    seasons = SerieSeasonFactory.create_batch(3)
    mock_serie_repository = mocker.Mock()
    mock_serie_repository.matching.return_value = None
    mock_query_bus = mocker.Mock()
    mock_query_bus.ask.return_value = media
    mock_event_bus = mocker.Mock()
    handler = SerieCreateCommandHandler(mock_serie_repository, mock_query_bus, mock_event_bus)
    command = SerieCreateCommand(
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

    handler.handle(command)

    mock_serie_repository.save.assert_called_once()
