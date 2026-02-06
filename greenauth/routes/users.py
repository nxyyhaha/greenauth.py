from typing import Any, Dict

from .client import APIClient


class UsersHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def disable_user(self, app_id: str, username: str) -> Dict[str, Any]:
        """Disable a user"""
        return await self.client.request(
            "POST", f"/api/key/dashboard/apps/{app_id}/users/{username}/disable"
        )

    async def enable_user(self, app_id: str, username: str) -> Dict[str, Any]:
        """Enable a user"""
        return await self.client.request(
            "POST", f"/api/key/dashboard/apps/{app_id}/users/{username}/enable"
        )
