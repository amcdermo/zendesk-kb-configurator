# Zendesk Knowledge Base Configurator

A Python tool to configure and manage Zendesk knowledge base settings programmatically.

## Features

- Configure knowledge base settings via Zendesk API
- Manage categories, sections, and articles
- Bulk operations for knowledge base content
- Export and import configurations

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```
ZENDESK_SUBDOMAIN=your_subdomain
ZENDESK_EMAIL=your_email@example.com
ZENDESK_API_TOKEN=your_api_token
```

## Usage

```python
from zendesk_kb_configurator import ZendeskKBConfigurator

# Initialize the configurator
kb = ZendeskKBConfigurator()

# Example: List all categories
categories = kb.get_categories()
```

## Development

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 src/
```

## License

MIT License
