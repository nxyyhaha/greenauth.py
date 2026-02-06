from typing import Dict, Any
from .client import APIClient


class SecurityHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def ban_hwid(self, app_id: str, hwid: str) -> Dict[str, Any]:
        """Ban an HWID"""
        payload = {"hwid": hwid}
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/ban/hwid",
            payload
        )

    async def unban_hwid(self, app_id: str, hwid: str) -> Dict[str, Any]:
        """Unban an HWID"""
        payload = {"hwid": hwid}
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/unban/hwid",
            payload
        )

    async def ban_ip(self, app_id: str, ip: str) -> Dict[str, Any]:
        """Ban an IP address"""
        payload = {"ip": ip}
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/ban/ip",
            payload
        )

    async def unban_ip(self, app_id: str, ip: str) -> Dict[str, Any]:
        """Unban an IP address"""
        payload = {"ip": ip}
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/unban/ip",
            payload
        )