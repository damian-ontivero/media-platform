import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv(".env", override=True)


class PostgresDB:

    @staticmethod
    def create_session(
        db_user: str, db_pass: str, db_host: str, db_port: str, db_name: str, db_autocommit: bool, db_verbose: bool
    ):
        engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}", echo=db_verbose)

        return sessionmaker(bind=engine, autocommit=db_autocommit)


PostgresSession = PostgresDB.create_session(
    db_user=os.getenv("POSTGRES_USER"),
    db_pass=os.getenv("POSTGRES_PASS"),
    db_host=os.getenv("POSTGRES_HOST"),
    db_port=os.getenv("POSTGRES_PORT"),
    db_name=os.getenv("POSTGRES_NAME"),
    db_autocommit=False,
    db_verbose=False,
)


class Base(DeclarativeBase):
    pass
