# Media Platform Backend

This repository contains the backend for the Media Platform project.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/damian-ontivero/media-platform.git`
2. Create the virtual environment and activate it:
    - `python3 -m venv var/venv`
    - `source var/venv/bin/activate`
3. Install dependencies:
    - `python -m pip install --upgrade pip`
    - `pip install poetry~=1.8`
    - `poetry install`
4. Run: poetry run uvicorn src.apps.channel.api.v0.main:app --reload


## Run with Docker

To build and run the application with Docker, you can use the follow command:

`docker compose -f ./etc/compose/compose.yaml up -d --build`

## Usage

Once the server is running, you can access to:

Swagger: http://127.0.0.1:8000/swagger

Documentation: http://127.0.0.1:8000/documentation


## Information:

This project implement:

1. Domain-Driven Design
2. Hexagonal Architecture
3. Dependency Injection
4. Repository Pattern

Note: Also is ready to implement CQRS.

### Domain-Driven Design

Media Platform domain has (at the moment) one bounded context (Chanel) with two aggregates: Channel and Content.


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
