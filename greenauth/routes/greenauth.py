import os
from .client import APIClient
from .auth import AuthHandler
from .apps import AppsHandler
from .licenses import LicensesHandler
from .users import UsersHandler
from .security import SecurityHandler
from .webhooks import WebhooksHandler


class GreenAuthAPI:
    def __init__(self, server_url: str | None = None, api_key: str | None = None):
        self.client = APIClient(server_url, api_key)
        
        self.auth = AuthHandler(self.client)
        self.apps = AppsHandler(self.client)
        self.licenses = LicensesHandler(self.client)
        self.users = UsersHandler(self.client)
        self.security = SecurityHandler(self.client)
        self.webhooks = WebhooksHandler(self.client)


default_api = GreenAuthAPI()

async def register(
    username: str,
    password: str,
    license_key: str,
    hwid: str,
    app_id: str,
    app_name: str
):
    """Register a new user using default API instance"""
    return await default_api.auth.register(username, password, license_key, hwid, app_id, app_name)

async def login(
    username: str,
    password: str,
    hwid: str,
    app_id: str,
    app_name: str
):
    """Login using default API instance"""
    return await default_api.auth.login(username, password, hwid, app_id, app_name)

async def get_apps():
    """Get apps using default API instance"""
    return await default_api.apps.get_apps()

async def reset_hwid(
    app_id: str, 
    username: str, 
    password: str, 
    license_key: str
):
    """Reset HWID using default API instance"""
    return await default_api.apps.reset_hwid(app_id, username, password, license_key)