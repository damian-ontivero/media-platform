import pytest
from src.contexts.backoffice.movies.application.query import (
    MovieSearchByCriteriaQuery,
    MovieSearchByCriteriaQueryHandler,
)
from src.contexts.backoffice.movies.application.services import MovieSearcher
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


@pytest.mark.asyncio
async def test_searcher__ok(mock_movie_repository):
    movies = MovieFactory.create_batch(10)
    mock_movie_repository.matching.return_value = movies
    searcher = MovieSearcher(mock_movie_repository)
    query = MovieSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = MovieSearchByCriteriaQueryHandler(searcher)

    found_movies = await handler.handle(query)

    assert len(found_movies) == 10


@pytest.mark.asyncio
async def test_searcher__with_criteria__ok(mock_movie_repository):
    movie = MovieFactory(title="The Godfather")
    mock_movie_repository.matching.return_value = [movie]
    searcher = MovieSearcher(mock_movie_repository)
    query = MovieSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = MovieSearchByCriteriaQueryHandler(searcher)

    found_movies = await handler.handle(query)

    assert found_movies == [movie]
