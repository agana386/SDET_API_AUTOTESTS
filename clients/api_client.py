import requests


class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def create_post(self, payload: dict):
        return requests.post(f"{self.BASE_URL}/posts", json=payload)

    def get_post(self, post_id: int):
        return requests.get(f"{self.BASE_URL}/posts/{post_id}")

    def get_all_posts(self):
        return requests.get(f"{self.BASE_URL}/posts")

    def patch_post(self, post_id: int, payload: dict):
        return requests.patch(f"{self.BASE_URL}/posts/{post_id}", json=payload)

    def delete_post(self, post_id: int):
        return requests.delete(f"{self.BASE_URL}/posts/{post_id}")