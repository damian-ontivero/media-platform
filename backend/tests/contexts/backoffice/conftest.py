import dotenv
import pytest


dotenv.load_dotenv("src/apps/backoffice/.env", override=True)


@pytest.fixture
def mock_command_bus(mocker):
    return mocker.AsyncMock()


@pytest.fixture
def mock_query_bus(mocker):
    return mocker.AsyncMock()


@pytest.fixture
def mock_event_bus(mocker):
    return mocker.AsyncMock()
