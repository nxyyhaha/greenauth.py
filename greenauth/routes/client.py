import aiohttp
import os
from typing import Dict, Any


class APIClient:
    def __init__(self, server_url: str | None = None, api_key: str | None = None):
        self.server = server_url or os.getenv("GREENAUTH_SERVER", "https://greenauth.co.uk")
        self.api_key = api_key or os.getenv("GREENAUTH_API_KEY")
        
        if not self.api_key:
            raise ValueError("API key is required")

    async def request(self, method: str, endpoint: str, json_body: Dict | None = None) -> Dict[str, Any]:
        headers = {
            "Content-Type": "application/json",
        }
        
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        url = f"{self.server}{endpoint}"
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.request(method, url, json=json_body, timeout=15) as response:
                data = await response.json()
                if response.status >= 400:
                    raise RuntimeError(data.get("detail", data))
                return data