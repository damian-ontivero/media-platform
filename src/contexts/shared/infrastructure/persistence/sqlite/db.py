import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()


class SQLiteDB:

    @staticmethod
    def create_session(
        db_uri: str,
        db_autocommit: bool,
        db_verbose: bool,
    ):
        engine = create_engine(
            db_uri,
            connect_args={"check_same_thread": False},
            echo=db_verbose,
        )

        return sessionmaker(bind=engine, autocommit=db_autocommit)


SqliteSession = SQLiteDB.create_session(
    db_uri=os.getenv("SQLITE_DB_URI"),
    db_autocommit=False,
    db_verbose=False,
)


class Base(DeclarativeBase):
    pass
