import faker
import pytest
from src.contexts.backoffice.movies.application.query import MovieFindByIdQuery, MovieFindByIdQueryHandler
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


def test_movie_finder__ok(mocker) -> None:
    movie = MovieFactory()
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = movie
    query = MovieFindByIdQuery(movie.id.value)
    handler = MovieFindByIdQueryHandler(mock_movie_repository)

    found_movie = handler.handle(query)

    assert found_movie == movie


def test_movie_finder__not_found(mocker) -> None:
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.search.return_value = None
    query = MovieFindByIdQuery(faker.Faker().uuid4())
    handler = MovieFindByIdQueryHandler(mock_movie_repository)

    with pytest.raises(Exception):
        handler.handle(query)
