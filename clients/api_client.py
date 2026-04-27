# clients/api_client.py
import requests
import functools


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
    @check_status(200, 201)
    def _get(self, url: str) -> requests.Response:
        return requests.get(url)

    @check_status(201)
    def _post(self, url: str, payload: dict) -> requests.Response:
        return requests.post(url, json=payload)

    @check_status(200)
    def _patch(self, url: str, payload: dict) -> requests.Response:
        return requests.patch(url, json=payload)

    @check_status(200)
    def _delete(self, url: str) -> requests.Response:
        return requests.delete(url)