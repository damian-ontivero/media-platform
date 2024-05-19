from src.backoffice.contexts.content.movies.domain import Movie
from src.backoffice.contexts.shared.infrastructure.criteria import criteria_to_sqlalchemy_query

from .movie import PostgresMovie


class PostgresMovieRepository:
    def __init__(self, session):
        self.session = session

    def search_all(self) -> list[Movie]:
        with self.session() as session:
            movies_db = session.query(PostgresMovie).all()
            return [Movie.from_primitives(movie.id, movie.title, movie.metadata) for movie in movies_db]

    def search(self, id: str) -> Movie | None:
        with self.session() as session:
            movie_db = session.get(PostgresMovie, id)
            if movie_db is None:
                return None
            return Movie.from_primitives(movie_db.id, movie_db.title, movie_db.metadata)

    def matching(self, criteria) -> list[Movie]:
        with self.session() as session:
            query = session.query(PostgresMovie)
            query = criteria_to_sqlalchemy_query(query, PostgresMovie, criteria)
            movies_db = query.all()
            return [Movie.from_primitives(movie_db.id, movie_db.title, movie_db.links) for movie_db in movies_db]

    def count(self) -> int:
        with self.session() as session:
            return session.query(PostgresMovie).count()

    def save(self, movie: Movie) -> None:
        with self.session() as session:
            movie_db = PostgresMovie(id=movie.id.value, title=movie.title, links=movie.links)
            session.add(movie_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self.session() as session:
            movie_db = session.get(PostgresMovie, id)
            session.delete(movie_db)
            session.commit()
