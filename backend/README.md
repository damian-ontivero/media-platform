# Media Platform Backend

This repository contains the backend for the Media Platform project.

## Installation

Requirements:

1. `python~=3.12`
2. `virtualenv~=20.25`

To install and run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/damian-ontivero/media_platform.git`
2. Create the virtual environment and activate it:
    - `python -m venv var/venv`
    - `source var/venv/bin/activate`
3. Install dependencies:
    - `python -m pip install --upgrade pip`
    - `pip install poetry~=1.8`
    - `poetry install`
4. Execute: `poetry run uvicorn src.apps.backoffice.api.v0.main:app --reload`


## Run with Docker

To build and run the application with Docker, you can execute the following command from the root directory:

`docker compose -f ./etc/compose/compose.yaml up -d --build`

## Usage

Once the server is running, you can access to:

Swagger: http://127.0.0.1:8000/swagger

Documentation: http://127.0.0.1:8000/documentation


## About

Stack:

1. FastAPI (https://fastapi.tiangolo.com)
2. SQLAlchemy (https://www.sqlalchemy.org)
3. Alembic (https://alembic.sqlalchemy.org)
4. SQLite (https://www.sqlite.org)
5. Docker (https://www.docker.com)
6. ditainer (https://test.pypi.org/project/ditainer/ propietario)

Another database engine like MySQL or PostgreSQL could be used.
As the project implements the repository pattern and hexagonal architecture, the decision to change the
DBMS should not be a problem. At the moment the migrations are running in the docker build and this is not the best aproach.
If we would be using a CI/CD pipeline, de CD should be in charge of run migrations and the CI should deploy the env vars also. 


This project implement:

1. Domain-Driven Design
2. Hexagonal Architecture
3. Dependency Injection
4. Repository Pattern

**Note:** Also is ready to implement CQRS.

### Domain-Driven Design

Media Platform domain has (at the moment) one bounded context (Content) with two aggregates: Movies and Series.


### Filter in API

In order to be able to filter the data retrive, the API implement the Criteria Pattern.
The criteria must be a base64 encoded *INLINE* JSON string with the following structure:

```json    
{
    "filter": {
    "conjunction": "AND",
    "conditions": [
        {
            "field": "channel_id",
            "operator": "CONTAINS",
            "value": "1"
        }
        ]
    },
    "sort": [
        {
        "field": "rating",
        "direction": "ASC"
        }
    ],
    "page_size": 15,
    "page_number": 1
}
```

To convert the JSON in one line you can use: https://www.text-utils.com/json-formatter/

To convert the JSON into base64 you can use: https://www.base64encode.org/
