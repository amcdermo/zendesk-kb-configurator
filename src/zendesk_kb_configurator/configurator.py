"""Main configurator class for Zendesk Knowledge Base."""

import os
from typing import Dict, List, Optional
import requests
from dotenv import load_dotenv


class ZendeskKBConfigurator:
    """Zendesk Knowledge Base Configurator for managing KB content and settings."""

    def __init__(
        self,
        subdomain: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
    ):
        """Initialize the configurator with Zendesk credentials.

        Args:
            subdomain: Zendesk subdomain (e.g., 'mycompany' for mycompany.zendesk.com)
            email: Zendesk user email
            api_token: Zendesk API token

        If credentials are not provided, they will be loaded from environment variables.
        """
        load_dotenv()

        self.subdomain = subdomain or os.getenv("ZENDESK_SUBDOMAIN")
        self.email = email or os.getenv("ZENDESK_EMAIL")
        self.api_token = api_token or os.getenv("ZENDESK_API_TOKEN")

        if not all([self.subdomain, self.email, self.api_token]):
            raise ValueError(
                "Missing required credentials. Provide subdomain, email, and api_token "
                "or set ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, and ZENDESK_API_TOKEN environment variables."
            )

        self.base_url = f"https://{self.subdomain}.zendesk.com/api/v2"
        self.auth = (f"{self.email}/token", self.api_token)

    def _request(
        self, method: str, endpoint: str, **kwargs
    ) -> requests.Response:
        """Make an API request to Zendesk.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., '/help_center/categories')
            **kwargs: Additional arguments to pass to requests

        Returns:
            Response object from requests
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, auth=self.auth, **kwargs)
        response.raise_for_status()
        return response

    def get_categories(self) -> List[Dict]:
        """Get all knowledge base categories.

        Returns:
            List of category dictionaries
        """
        response = self._request("GET", "/help_center/categories")
        return response.json().get("categories", [])

    def get_sections(self, category_id: Optional[int] = None) -> List[Dict]:
        """Get knowledge base sections, optionally filtered by category.

        Args:
            category_id: Optional category ID to filter sections

        Returns:
            List of section dictionaries
        """
        if category_id:
            endpoint = f"/help_center/categories/{category_id}/sections"
        else:
            endpoint = "/help_center/sections"

        response = self._request("GET", endpoint)
        return response.json().get("sections", [])

    def get_articles(self, section_id: Optional[int] = None) -> List[Dict]:
        """Get knowledge base articles, optionally filtered by section.

        Args:
            section_id: Optional section ID to filter articles

        Returns:
            List of article dictionaries
        """
        if section_id:
            endpoint = f"/help_center/sections/{section_id}/articles"
        else:
            endpoint = "/help_center/articles"

        response = self._request("GET", endpoint)
        return response.json().get("articles", [])
