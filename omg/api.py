import httpx
from .constants import API_URL
from .errors import RequestError
from httpx import Client
from typing import Optional


class API:
    def __init__(self, key: Optional[str] = None, email: Optional[str] = None):
        self.http: Client = httpx.Client(base_url=API_URL)
        self.key = key
        self.email = email

    def request(self, path, method="GET", body=None):
        req = self.http.request(
            method=method,
            url=path,
            json=body,
            headers={
                "Authorization": f"Bearer {self.key}"
            } if self.key else {}
        )

        j = req.json()
        if not j["request"]["success"]:
            raise RequestError(j['response']['message'])
        else:
            return j
