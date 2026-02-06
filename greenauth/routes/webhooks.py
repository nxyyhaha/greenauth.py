from typing import Dict, Any, List, Optional
from .client import APIClient


class WebhooksHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def create_webhook(
        self, app_id: str, url: str, events: List[str], secret: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new webhook"""
        payload = {"url": url, "events": events}
        if secret:
            payload["secret"] = secret

        return await self.client.request(
            "POST", f"/api/key/dashboard/apps/{app_id}/webhooks", payload
        )

    async def list_webhooks(self, app_id: str) -> List[Dict[str, Any]]:
        """List all webhooks for an application"""
        response = await self.client.request(
            "GET", f"/api/key/dashboard/apps/{app_id}/webhooks"
        )
        return response if isinstance(response, list) else [response]

    async def delete_webhook(self, app_id: str, webhook_id: str) -> Dict[str, Any]:
        """Delete a webhook"""
        return await self.client.request(
            "DELETE", f"/api/key/dashboard/apps/{app_id}/webhooks/{webhook_id}"
        )
