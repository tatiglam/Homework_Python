import pytest
import time
from api_client import YougileAPI
from config import Config


def pytest_configure(config):
    if not Config.TOKEN:
        pytest.exit("YOUGILE_TOKEN not set", returncode=1)


@pytest.fixture
def api_client():
    client = YougileAPI()
    yield client
    client.close()


@pytest.fixture
def test_project(api_client):
    title = f"Test_Project_{int(time.time())}"
    response = api_client.create_project(title)
    assert response.status_code == 201
    project_id = response.json().get("id")
    yield project_id
