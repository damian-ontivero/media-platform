import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv(".env", override=True)


class PostgresDB:
    """
    PostgresDB class to create a session with the database.
    """

    @staticmethod
    def create_session(
        username: str, password: str, host: str, port: str, database: str, autocommit: bool, verbose: bool
    ):
        engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}", echo=verbose)

        return sessionmaker(bind=engine, autocommit=autocommit)


PostgresSession = PostgresDB.create_session(
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASS"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DATABASE"),
    autocommit=False,
    verbose=False,
)


class Base(DeclarativeBase):
    """
    Base class for all ORM classes to inherit from.
    """

    pass
