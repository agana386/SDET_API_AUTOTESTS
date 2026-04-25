import pytest
from clients.api_client import ApiClient


@pytest.fixture
def client():
    return ApiClient()


@pytest.fixture
def created_post(client):
    payload = {
        "title": "test",
        "body": "test body",
        "userId": 1
    }
    post = client.create_post(payload)
    # jsonplaceholder всегда возвращает id=101, но реально хранит только 1-100
    # подменяем на реально существующий id
    post.id = 1
    return post