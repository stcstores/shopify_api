"""Exceptions for the shopify_api package."""
from typing import Any, Mapping


class LoginCredentialsNotSetError(ValueError):
    """Exception raised when creating an API session without credentials set."""

    def __init__(self, *args: list[Any], **kwargs: Mapping[Any, Any]) -> None:
        """Exception raised when creating an API session without credentials set."""
        super().__init__("SHOP_URL, API_VERSION and API_PASSWORD must be set.")
