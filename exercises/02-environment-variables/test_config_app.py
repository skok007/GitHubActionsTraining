import os
from unittest.mock import MagicMock, patch

import pytest
from config_app import ConfigApp


def test_config_app_initialization():
    """Test that the ConfigApp initializes correctly with environment variables."""
    with patch.dict(
        os.environ,
        {
            "API_URL": "https://test-api.example.com",
            "API_KEY": "test-api-key",
            "DEBUG_MODE": "True",
        },
    ):
        app = ConfigApp()
        config = app.get_config()

        assert config["api_url"] == "https://test-api.example.com"
        assert config["api_key"] == "********"  # API key should be masked
        assert config["debug_mode"] is True


def test_config_app_missing_api_key():
    """Test that the ConfigApp raises an error when API_KEY is missing."""
    with patch.dict(os.environ, clear=True):
        with pytest.raises(
            ValueError, match="API_KEY environment variable is required"
        ):
            ConfigApp()


def test_config_app_default_values():
    """Test that the ConfigApp uses default values when environment variables are missing."""
    with patch.dict(os.environ, {"API_KEY": "test-api-key"}):
        app = ConfigApp()
        config = app.get_config()

        assert config["api_url"] == "https://api.example.com"  # Default value
        assert config["debug_mode"] is False  # Default value


@patch("requests.get")
def test_make_api_request(mock_get):
    """Test that the make_api_request method works correctly."""
    # Set up the mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": "test data"}
    mock_get.return_value = mock_response

    # Set up environment variables
    with patch.dict(
        os.environ,
        {
            "API_URL": "https://test-api.example.com",
            "API_KEY": "test-api-key",
            "DEBUG_MODE": "True",
        },
    ):
        app = ConfigApp()
        result = app.make_api_request("test-endpoint")

        # Verify the request was made correctly
        mock_get.assert_called_once_with(
            "https://test-api.example.com/test-endpoint",
            headers={
                "Authorization": "Bearer test-api-key",
                "Content-Type": "application/json",
            },
        )

        assert result == {"data": "test data"}


@patch("requests.get")
def test_validate_connection_success(mock_get):
    """Test that the validate_connection method returns True when the API is healthy."""
    # Set up the mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "ok"}
    mock_get.return_value = mock_response

    # Set up environment variables
    with patch.dict(
        os.environ,
        {"API_URL": "https://test-api.example.com", "API_KEY": "test-api-key"},
    ):
        app = ConfigApp()
        result = app.validate_connection()

        assert result is True


@patch("requests.get")
def test_validate_connection_failure(mock_get):
    """Test that the validate_connection method returns False when the API is not healthy."""
    # Set up the mock response to raise an exception
    mock_get.side_effect = Exception("Connection error")

    # Set up environment variables
    with patch.dict(
        os.environ,
        {
            "API_URL": "https://test-api.example.com",
            "API_KEY": "test-api-key",
            "DEBUG_MODE": "True",
        },
    ):
        app = ConfigApp()
        result = app.validate_connection()

        assert result is False
