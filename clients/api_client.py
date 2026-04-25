import requests
import functools
from typing import List
from config import BASE_URL
from models.entity import Post, PostPartial


def check_status(*default_codes):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, expected_status: list[int] | None = None, **kwargs):
            response = func(*args, **kwargs)
            codes = expected_status if expected_status is not None else list(default_codes)
            assert response.status_code in codes, (
                f"{func.__name__}: ожидался статус {codes}, получен {response.status_code}"
            )
            return response
        return wrapper
    return decorator


class ApiClient:
    BASE_URL = BASE_URL

    @check_status(201)
    def _create_post_raw(self, payload: dict) -> requests.Response:
        return requests.post(f"{self.BASE_URL}/posts", json=payload)

    @check_status(200)
    def _get_post_raw(self, post_id: int) -> requests.Response:
        return requests.get(f"{self.BASE_URL}/posts/{post_id}")

    @check_status(200)
    def _get_all_posts_raw(self) -> requests.Response:
        return requests.get(f"{self.BASE_URL}/posts")

    @check_status(200)
    def _patch_post_raw(self, post_id: int, payload: dict) -> requests.Response:
        return requests.patch(f"{self.BASE_URL}/posts/{post_id}", json=payload)

    @check_status(200)
    def _delete_post_raw(self, post_id: int) -> requests.Response:
        return requests.delete(f"{self.BASE_URL}/posts/{post_id}")

    def create_post(self, payload: dict) -> Post:
        return Post(**self._create_post_raw(payload).json())

    def get_post(self, post_id: int) -> Post:
        return Post(**self._get_post_raw(post_id).json())

    def get_all_posts(self) -> List[Post]:
        return [Post(**item) for item in self._get_all_posts_raw().json()]

    def patch_post(self, post_id: int, payload: dict) -> PostPartial:
        return PostPartial(**self._patch_post_raw(post_id, payload).json())

    def delete_post(self, post_id: int) -> dict:
        return self._delete_post_raw(post_id).json()