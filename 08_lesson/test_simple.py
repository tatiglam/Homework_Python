from config import Config
from api_client import YougileAPI


def test_simple():
    assert True


def test_config():
    assert Config.BASE_URL == "https://ru.yougile.com/api-v2"


def test_api_import():
    assert YougileAPI is not None
