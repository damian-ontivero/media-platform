import faker
import pytest
from src.contexts.backoffice.movies.application.query import MovieFindByIdQuery, MovieFindByIdQueryHandler
from src.contexts.backoffice.movies.application.services import MovieFinder
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


@pytest.mark.asyncio
async def test_movie_finder__ok(mock_movie_repository) -> None:
    movie = MovieFactory()
    mock_movie_repository.search.return_value = movie
    finder = MovieFinder(mock_movie_repository)
    query = MovieFindByIdQuery(movie.id.value)
    handler = MovieFindByIdQueryHandler(finder)

    found_movie = await handler.handle(query)

    assert found_movie == movie


@pytest.mark.asyncio
async def test_movie_finder__not_found(mock_movie_repository) -> None:
    mock_movie_repository.search.return_value = None
    finder = MovieFinder(mock_movie_repository)
    query = MovieFindByIdQuery(faker.Faker().uuid4())
    handler = MovieFindByIdQueryHandler(finder)

    with pytest.raises(Exception):
        await handler.handle(query)
