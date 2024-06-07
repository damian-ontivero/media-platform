from sqlalchemy.orm import Session
from src.contexts.backoffice.movies.domain import Movie, MovieRepository
from src.contexts.shared.infrastructure.criteria import criteria_to_sqlalchemy_query

from .movie import PostgresMovie


class PostgresMovieRepository(MovieRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def search_all(self) -> list[Movie]:
        with self._session() as session:
            query = session.query(PostgresMovie)
            return [Movie.from_primitives(**movie_db.to_primitives()) for movie_db in query.all()]

    def search(self, id: str) -> Movie | None:
        with self._session() as session:
            movie_db = session.get(PostgresMovie, id)
            if movie_db is None:
                return None
            return Movie.from_primitives(**movie_db.to_primitives())

    def matching(self, criteria) -> list[Movie]:
        with self._session() as session:
            query = session.query(PostgresMovie)
            query = criteria_to_sqlalchemy_query(query, PostgresMovie, criteria)
            return [Movie.from_primitives(**movie_db.to_primitives()) for movie_db in query.all()]

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgresMovie).count()

    def save(self, movie: Movie) -> None:
        with self._session() as session:
            movie_db = session.get(PostgresMovie, movie.id.value)
            if movie_db is None:
                movie_db = PostgresMovie.from_entity(movie)
                session.add(movie_db)
            else:
                movie_db.update(movie)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            movie_db = session.get(PostgresMovie, id)
            session.delete(movie_db)
            session.commit()
