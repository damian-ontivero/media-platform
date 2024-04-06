FROM python:3.12.2

RUN mkdir -p /app

WORKDIR /app

ENV PYTHONPATH=/app
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

COPY ./media_platform/backoffice ./media_platform/backoffice
COPY ./poetry.lock ./pyproject.toml
COPY ./pyproject.toml ./pyproject.toml

RUN python -m pip install --upgrade pip

RUN pip install poetry~=1.8

RUN poetry install

CMD ["poetry", "run", "uvicorn", "media_platform.backoffice.apps.channel.api.v0.main:app", "--host", "0.0.0.0", "--port", "8000"]
