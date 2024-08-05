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
    - `pip install pdm`
    - `pdm install`
4. Execute: `pdm bo:api`


## Run with Docker

To build and run the application with Docker, you can execute the following command from the root directory:

`docker compose -f ./etc/compose/compose.yaml up -d --build`

## Usage

Once the server is running, you can access to:

Swagger: http://127.0.0.1:8000/swagger

Documentation: http://127.0.0.1:8000/documentation


## About

Software design:

- Domain-Driven Design (DDD)
- Clean Architecture
- Command and Query Responsibility Segregation (CQRS)

Stack:

- FastAPI (https://fastapi.tiangolo.com)
- PostgreSQL (https://www.postgresql.org)
- SQLAlchemy (https://www.sqlalchemy.org)
- Alembic (https://alembic.sqlalchemy.org)
- Docker (https://www.docker.com)
- ditainer (https://test.pypi.org/project/ditainer propietario)

Another RDBMS could be used.
As the project implements the repository pattern and clean architecture, the decision to change the
DBMS should not be a problem. At the moment the migrations are running in the docker build and this is not the best aproach.
If we would be using a CI/CD pipeline, de CD should be in charge of run migrations and the CI should deploy the env vars also. 


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


pdm add aio-pika alembic cryptography ditainer "fastapi>=0.111.0, <1.0.0" moviepy python-multipart python-dotenv psycopg2-binary sqlalchemy uvicorn werkzeug
pdm add -dG dev ipdb
pdm add -dG format ruff
pdm add -dG test factory-boy pytest pytest-asyncio pytest-mock