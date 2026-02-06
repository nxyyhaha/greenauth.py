from typing import Dict, Any
from .client import APIClient


class AuthHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def register(
        self,
        username: str,
        password: str,
        license_key: str,
        hwid: str,
        app_id: str,
        app_name: str,
    ) -> Dict[str, Any]:
        """Register a new user with username/password and license key"""
        payload = {
            "username": username,
            "password": password,
            "license_key": license_key,
            "hwid": hwid,
            "app_id": app_id,
            "app_name": app_name,
        }
        return await self.client.request("POST", "/register", payload)

    async def login(
        self, username: str, password: str, hwid: str, app_id: str, app_name: str
    ) -> Dict[str, Any]:
        """Authenticate a user"""
        payload = {
            "username": username,
            "password": password,
            "hwid": hwid,
            "app_id": app_id,
            "app_name": app_name,
        }
        return await self.client.request("POST", "/login", payload)
