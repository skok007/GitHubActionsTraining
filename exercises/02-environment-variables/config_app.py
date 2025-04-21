import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class ConfigApp:
    """A simple application that uses environment variables for configuration."""

    def __init__(self):
        # Get configuration from environment variables
        self.api_url = os.getenv("API_URL", "https://api.example.com")
        self.api_key = os.getenv("API_KEY")
        self.debug_mode = os.getenv("DEBUG_MODE", "False").lower() == "true"

        if not self.api_key:
            raise ValueError("API_KEY environment variable is required")

    def get_config(self):
        """Return the current configuration."""
        return {
            "api_url": self.api_url,
            "api_key": "********" if self.api_key else None,  # Mask the API key
            "debug_mode": self.debug_mode,
        }

    def make_api_request(self, endpoint):
        """Make a request to the API using the configured credentials."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        url = f"{self.api_url}/{endpoint}"

        if self.debug_mode:
            print(f"Making request to: {url}")

        response = requests.get(url, headers=headers)
        return response.json()

    def validate_connection(self):
        """Validate the connection to the API."""
        try:
            response = self.make_api_request("health")
            return response.get("status") == "ok"
        except Exception as e:
            if self.debug_mode:
                print(f"Connection error: {str(e)}")
            return False
