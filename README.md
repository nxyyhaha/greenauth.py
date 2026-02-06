# GreenAuth Python SDK

[![PyPI version](https://badge.fury.io/py/greenauth.svg)](https://badge.fury.io/py/greenauth)
[![Python versions](https://img.shields.io/pypi/pyversions/greenauth.svg)](https://pypi.org/project/greenauth/)
[![License](https://img.shields.io/badge/License-GNU-lime.svg)](https://opensource.org/licenses/gpl-3-0)

Official Python SDK for the GreenAuth authentication service.

## Installation

```bash
pip install greenauth
```

## Quick Start

```python
import asyncio
from greenauth import GreenAuthAPI

async def main():
    # Initialize with your API key
    api = GreenAuthAPI(api_key="your_api_key_here")
    
    # Register a new user
    result = await api.auth.register(
        username="testuser",
        password="SecurePass123!",
        license_key="GA-XXXX-XXXX-XXXX",
        hwid="device_hash_here",
        app_id="your_app_id",
        app_name="Your App Name"
    )
    print("Registration result:", result)
    
    # Login user
    login_result = await api.auth.login(
        username="testuser",
        password="SecurePass123!",
        hwid="device_hash_here",
        app_id="your_app_id",
        app_name="Your App Name"
    )
    print("Login result:", login_result)

asyncio.run(main())
```

## API Handlers

### Authentication
```python
# Register user
await api.auth.register(username, password, license_key, hwid, app_id, app_name)

# Login user
await api.auth.login(username, password, hwid, app_id, app_name)
```

### Applications
```python
# List all apps
apps = await api.apps.get_apps()

# Create new app
app = await api.apps.create_app("My App", description="My description")

# Get app details
details = await api.apps.get_app_details(app_id)

# Reset HWID
await api.apps.reset_hwid(app_id, username, password, license_key)
```

### Licenses
```python
# Create license
license = await api.licenses.create_license(app_id, days=30, max_hwids=3)

# Delete unused licenses
await api.licenses.delete_unused(app_id)
```

### Users
```python
# Disable user
await api.users.disable_user(app_id, username)

# Enable user
await api.users.enable_user(app_id, username)
```

### Security
```python
# Ban HWID
await api.security.ban_hwid(app_id, hwid)

# Unban HWID
await api.security.unban_hwid(app_id, hwid)

# Ban IP
await api.security.ban_ip(app_id, ip_address)

# Unban IP
await api.security.unban_ip(app_id, ip_address)
```

### Webhooks
```python
# Create webhook
webhook = await api.webhooks.create_webhook(
    app_id, 
    "https://your-webhook-url.com",
    events=["user.login", "user.register"],
    secret="webhook_secret"
)

# List webhooks
webhooks = await api.webhooks.list_webhooks(app_id)

# Delete webhook
await api.webhooks.delete_webhook(app_id, webhook_id)
```

## Configuration

You can configure the SDK in multiple ways:

```python
# Method 1: Direct parameters
api = GreenAuthAPI(
    server_url="https://greenauth.co.uk",
    api_key="your_api_key"
)

# Method 2: Environment variables
import os
os.environ["GREENAUTH_SERVER"] = "https://greenauth.co.uk"
os.environ["GREENAUTH_API_KEY"] = "your_api_key"

api = GreenAuthAPI()  # Will use environment variables
```

## Error Handling

The SDK raises `RuntimeError` for API errors:

```python
try:
    await api.auth.login("user", "pass", "hwid", "app_id", "app_name")
except RuntimeError as e:
    print(f"Authentication failed: {e}")
```

## Advanced Usage

### Using Custom Client
```python
from greenauth import APIClient, AuthHandler

client = APIClient(server_url="https://your-server.com", api_key="your_key")
auth = AuthHandler(client)
result = await auth.register(...)
```

### Individual Handlers
```python
from greenauth import AppsHandler, APIClient

client = APIClient(api_key="your_key")
apps = AppsHandler(client)
app_list = await apps.get_apps()
```


## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.

## Support

- [Documentation](https://greenauth.co.uk/docs)
- [Issues](https://github.com/nxyyhaha/greenauth.py/issues)
- [Discord](https://discord.gg/HYpmXsQJhP)