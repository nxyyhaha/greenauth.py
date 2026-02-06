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