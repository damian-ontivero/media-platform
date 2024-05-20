from src.contexts.backoffice.movies.domain.movie import Movie
from src.contexts.backoffice.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain.criteria import Criteria


class MovieSearcher:
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    def run(self, criteria: dict | None = None) -> list[Movie]:
        if criteria is None:
            return self.repository.search_all()
        return self.repository.matching(Criteria.from_primitives(**criteria))
