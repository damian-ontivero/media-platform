import pytest
from src.contexts.backoffice.movies.application.query import (
    MovieSearchByCriteriaQuery,
    MovieSearchByCriteriaQueryHandler,
)
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


@pytest.mark.asyncio
async def test_searcher__ok(mocker):
    movies = MovieFactory.create_batch(10)
    mock_content_repository = mocker.Mock()
    mock_content_repository.matching.return_value = movies
    query = MovieSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = MovieSearchByCriteriaQueryHandler(mock_content_repository)

    found_movies = await handler.handle(query)

    assert len(found_movies) == 10


@pytest.mark.asyncio
async def test_searcher__with_criteria__ok(mocker):
    movie = MovieFactory(title="The Godfather")
    mock_movie_repository = mocker.Mock()
    mock_movie_repository.matching.return_value = [movie]
    query = MovieSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = MovieSearchByCriteriaQueryHandler(mock_movie_repository)

    found_movies = await handler.handle(query)

    assert found_movies == [movie]
