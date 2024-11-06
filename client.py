import requests
from typing import Dict, Any, Optional


class AuroaClient:
    def __init__(self, base_url: str = ""):
        self.base_url = base_url
        self.default_headers: Dict[str, str] = {}

    def set_default_headers(self, headers: Dict[str, str]):
        self.default_headers.update(headers)

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        return self._request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        return self._request("POST", path, json=json, headers=headers)

    def put(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        return self._request("PUT", path, json=json, headers=headers)

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None):
        return self._request("DELETE", path, headers=headers)

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        url = self.base_url + path
        combined_headers = {
            **self.default_headers,
            **(headers or {}),
        }  
        try:
            response = requests.request(
                method, url, params=params, json=json, headers=combined_headers
            )
            response.raise_for_status()
            return (
                response.json()
                if response.headers.get("Content-Type") == "application/json"
                else response.text
            )
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
