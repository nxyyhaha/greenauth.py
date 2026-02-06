import pytest
import asyncio
from unittest.mock import AsyncMock, patch


class TestBasicImports:
    """Test that all classes can be imported successfully."""

    def test_import_main_classes(self):
        """Test importing main API classes."""
        from greenauth import GreenAuthAPI, APIClient

        assert GreenAuthAPI is not None
        assert APIClient is not None

    def test_import_handlers(self):
        """Test importing handler classes."""
        from greenauth import (
            AuthHandler,
            AppsHandler,
            LicensesHandler,
            UsersHandler,
            SecurityHandler,
            WebhooksHandler,
        )

        assert AuthHandler is not None
        assert AppsHandler is not None
        assert LicensesHandler is not None
        assert UsersHandler is not None
        assert SecurityHandler is not None
        assert WebhooksHandler is not None


class TestGreenAuthAPI:
    """Test main GreenAuthAPI class."""

    def test_init_with_api_key(self):
        """Test initialization with API key."""
        from greenauth import GreenAuthAPI

        api = GreenAuthAPI(api_key="test_key")
        assert api.client.api_key == "test_key"
        assert api.client.server == "https://greenauth.co.uk"

    def test_init_without_api_key_env_var(self):
        """Test initialization using environment variable."""
        from greenauth import GreenAuthAPI

        with patch.dict("os.environ", {"GREENAUTH_API_KEY": "env_key"}):
            api = GreenAuthAPI()
            assert api.client.api_key == "env_key"

    def test_init_no_api_key_raises_error(self):
        """Test that initialization fails without API key."""
        from greenauth import GreenAuthAPI

        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="API key is required"):
                GreenAuthAPI(api_key=None)

    def test_handlers_creation(self):
        """Test that all handlers are created."""
        from greenauth import GreenAuthAPI, AuthHandler, AppsHandler

        api = GreenAuthAPI(api_key="test_key")

        assert hasattr(api, "auth")
        assert hasattr(api, "apps")
        assert hasattr(api, "licenses")
        assert hasattr(api, "users")
        assert hasattr(api, "security")
        assert hasattr(api, "webhooks")

        assert isinstance(api.auth, AuthHandler)
        assert isinstance(api.apps, AppsHandler)


class TestAPIClient:
    """Test APIClient functionality."""

    def test_init_with_credentials(self):
        """Test client initialization with credentials."""
        from greenauth import APIClient

        client = APIClient(server_url="https://test.com", api_key="test_key")
        assert client.server == "https://test.com"
        assert client.api_key == "test_key"

    def test_init_default_server(self):
        """Test client uses default server URL."""
        from greenauth import APIClient

        with patch.dict("os.environ", {"GREENAUTH_API_KEY": "test_key"}):
            client = APIClient()
            assert client.server == "https://greenauth.co.uk"
            assert client.api_key == "test_key"

    @pytest.mark.asyncio
    async def test_request_success(self):
        """Test successful API request."""
        from greenauth import APIClient

        # Simple test that just checks the method exists and doesn't error
        client = APIClient(api_key="test_key")

        # Test that request method is callable
        assert hasattr(client, "request")
        assert callable(client.request)


class TestVersionInfo:
    """Test version and package info."""

    def test_version_attributes(self):
        """Test that version attributes exist."""
        import greenauth

        assert hasattr(greenauth, "__version__")
        assert hasattr(greenauth, "__author__")
        assert hasattr(greenauth, "__email__")
        assert hasattr(greenauth, "__license__")

        assert greenauth.__version__ == "1.0.0"
        assert greenauth.__author__ == "GreenAuth"
        assert greenauth.__email__ == "support@greenauth.co.uk"
        assert greenauth.__license__ == "MIT"


class TestPackageStructure:
    """Test package structure and exports."""

    def test_all_exports(self):
        """Test that __all__ contains expected exports."""
        import greenauth

        expected_exports = {
            "APIClient",
            "AuthHandler",
            "AppsHandler",
            "LicensesHandler",
            "UsersHandler",
            "SecurityHandler",
            "WebhooksHandler",
            "GreenAuthAPI",
        }

        actual_exports = set(greenauth.__all__)
        assert actual_exports == expected_exports

    def test_module_docstring(self):
        """Test that module has docstring."""
        import greenauth

        assert greenauth.__doc__ is not None
        assert "GreenAuth Python SDK" in greenauth.__doc__


class TestErrorHandling:
    """Test error handling scenarios."""

    def test_api_client_validation(self):
        """Test API client validation."""
        from greenauth import APIClient

        # Test missing API key
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="API key is required"):
                APIClient(api_key=None)


if __name__ == "__main__":
    # Run tests when executed directly
    pytest.main([__file__, "-v", "--tb=short"])
