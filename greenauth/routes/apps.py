from typing import Dict, Any, List, Optional
from .client import APIClient


class AppsHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def get_apps(self) -> List[Dict[str, Any]]:
        """List all applications"""
        response = await self.client.request("GET", "/api/key/dashboard/apps")
        return response if isinstance(response, list) else [response]

    async def create_app(
        self,
        name: str,
        description: Optional[str] = None,
        version: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new application"""
        payload = {"name": name}
        if description:
            payload["description"] = description
        if version:
            payload["version"] = version
            
        return await self.client.request("POST", "/api/key/dashboard/apps/create", payload)

    async def get_app_details(self, app_id: str) -> Dict[str, Any]:
        """Get details for a specific application"""
        return await self.client.request("GET", f"/api/key/dashboard/apps/{app_id}")

    async def reset_hwid(
        self,
        app_id: str,
        username: str,
        password: str,
        license_key: str
    ) -> Dict[str, Any]:
        """Reset HWID for a license"""
        payload = {
            "username": username,
            "password": password,
            "license_key": license_key
        }
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/reset-hwid",
            payload
        )