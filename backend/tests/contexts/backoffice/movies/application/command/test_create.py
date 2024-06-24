import faker
from src.contexts.backoffice.movies.application.command import MovieCreateCommand, MovieCreateCommandHandler
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


def test_movie_creator__ok(mocker) -> None:
    media = MediaFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.matching.return_value = None
    mock_query_bus = mocker.Mock()
    mock_query_bus.ask.return_value = media
    handler = MovieCreateCommandHandler(mock_movie_repository, mock_query_bus)
    command = MovieCreateCommand(title=faker.Faker().name(), media_id=media.id.value)

    handler.handle(command)

    mock_movie_repository.save.assert_called_once()
