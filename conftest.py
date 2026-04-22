import pytest
from clients.api_client import ApiClient


@pytest.fixture
def client():
    return ApiClient()