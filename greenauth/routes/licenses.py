from typing import Dict, Any, Optional
from .client import APIClient


class LicensesHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def create_license(
        self,
        app_id: str,
        days: Optional[int] = None,
        max_hwids: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new license for an application"""
        payload = {}
        if days is not None:
            payload["days"] = days
        if max_hwids is not None:
            payload["max_hwids"] = max_hwids
        if metadata:
            payload["metadata"] = metadata
            
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/create-license",
            payload
        )

    async def delete_unused(self, app_id: str) -> Dict[str, Any]:
        """Delete unused licenses for an application"""
        return await self.client.request(
            "POST",
            f"/api/key/dashboard/apps/{app_id}/licenses/delete-unused"
        )