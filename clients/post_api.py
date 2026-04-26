from typing import List
from clients.api_client import ApiClient
from models.entity import Post, PostPartial
from config import BASE_URL


class PostApi(ApiClient):
    POSTS_URL = f"{BASE_URL}/posts"

    def create_post(self, payload: dict) -> Post:
        return Post(**self._post(self.POSTS_URL, payload).json())

    def get_post(self, post_id: int) -> Post:
        return Post(**self._get(f"{self.POSTS_URL}/{post_id}").json())

    def get_all_posts(self) -> List[Post]:
        return [Post(**item) for item in self._get(self.POSTS_URL).json()]

    def patch_post(self, post_id: int, payload: dict) -> PostPartial:
        return PostPartial(**self._patch(f"{self.POSTS_URL}/{post_id}", payload).json())

    def delete_post(self, post_id: int) -> dict:
        return self._delete(f"{self.POSTS_URL}/{post_id}").json()