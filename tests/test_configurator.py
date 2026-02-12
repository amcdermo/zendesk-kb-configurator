"""Tests for the ZendeskKBConfigurator class."""

import pytest
from unittest.mock import Mock, patch
from zendesk_kb_configurator import ZendeskKBConfigurator


class TestZendeskKBConfigurator:
    """Test suite for ZendeskKBConfigurator."""

    @patch.dict(
        "os.environ",
        {
            "ZENDESK_SUBDOMAIN": "test",
            "ZENDESK_EMAIL": "test@example.com",
            "ZENDESK_API_TOKEN": "test_token",
        },
    )
    def test_init_from_env(self):
        """Test initialization from environment variables."""
        configurator = ZendeskKBConfigurator()
        assert configurator.subdomain == "test"
        assert configurator.email == "test@example.com"
        assert configurator.api_token == "test_token"

    def test_init_missing_credentials(self):
        """Test that initialization fails without credentials."""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError):
                ZendeskKBConfigurator()

    @patch("zendesk_kb_configurator.configurator.requests.request")
    @patch.dict(
        "os.environ",
        {
            "ZENDESK_SUBDOMAIN": "test",
            "ZENDESK_EMAIL": "test@example.com",
            "ZENDESK_API_TOKEN": "test_token",
        },
    )
    def test_get_categories(self, mock_request):
        """Test getting categories."""
        mock_response = Mock()
        mock_response.json.return_value = {"categories": [{"id": 1, "name": "Test"}]}
        mock_request.return_value = mock_response

        configurator = ZendeskKBConfigurator()
        categories = configurator.get_categories()

        assert len(categories) == 1
        assert categories[0]["name"] == "Test"
