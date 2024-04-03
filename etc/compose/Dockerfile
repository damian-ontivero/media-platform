FROM python:3.12.2-alpine

RUN apk update
RUN apk upgrade

RUN mkdir -p /app

COPY ./src /app/src
COPY ./poetry.lock /app
COPY ./pyproject.toml /app
COPY ./.env /app
COPY ./database.db /app

WORKDIR /app

# The following lines are needed to run alembic migrations
# because for this project the database is inside the container.
COPY ./migrations /app/migrations
COPY ./alembic.ini /app/alembic.ini

RUN python -m pip install --upgrade pip

RUN pip install poetry~=1.8

RUN poetry install

# The following lines are needed to run alembic migrations
RUN poetry run alembic upgrade head

CMD ["poetry", "run", "uvicorn", "src.apps.channel.api.v0.main:app", "--host", "0.0.0.0", "--port", "8000"]
