FROM python:3.12.3-alpine

RUN mkdir -p /app

WORKDIR /app

ENV PYTHONPATH=/app
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

COPY ./src/apps/backoffice ./src/apps/backoffice
COPY ./src/contexts/backoffice ./src/contexts/backoffice
COPY ./src/contexts/shared ./src/contexts/shared

COPY ./poetry.lock ./pyproject.toml
COPY ./pyproject.toml ./pyproject.toml

RUN python -m pip install --upgrade pip

RUN pip install poetry~=1.8

RUN poetry install

CMD ["poetry", "run", "uvicorn", "src.apps.backoffice.api.v0.main:app", "--host", "0.0.0.0", "--port", "8000"]
