import pytest
from clients.post_api import PostApi


@pytest.fixture
def client():
    return PostApi()


@pytest.fixture
def created_post(client):
    payload = {
        "title": "test",
        "body": "test body",
        "userId": 1
    }
    post = client.create_post(payload)
    post.id = 1
    return post