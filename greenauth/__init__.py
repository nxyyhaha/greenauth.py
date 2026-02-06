"""
GreenAuth Python SDK

Official Python SDK for GreenAuth authentication service.
"""

from .routes.apps import AppsHandler
from .routes.auth import AuthHandler
from .routes.client import APIClient
from .routes.greenauth import GreenAuthAPI
from .routes.licenses import LicensesHandler
from .routes.security import SecurityHandler
from .routes.users import UsersHandler
from .routes.webhooks import WebhooksHandler

__version__ = "1.0.0"
__author__ = "GreenAuth"
__email__ = "support@greenauth.co.uk"
__license__ = "MIT"

__all__ = [
    "APIClient",
    "AuthHandler",
    "AppsHandler",
    "LicensesHandler",
    "UsersHandler",
    "SecurityHandler",
    "WebhooksHandler",
    "GreenAuthAPI",
]
