"""
Simple Flask web application for demonstrating GitHub Actions deployments.
"""

import os

from config import config
from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Load configuration based on environment
env = os.getenv("FLASK_ENV", "development")
app.config.from_object(config[env])


@app.route("/")
def index():
    """Return basic information about the application."""
    return jsonify(
        {
            "status": "ok",
            "environment": app.config["ENV"],
            "debug": app.config["DEBUG"],
            "version": app.config["VERSION"],
        }
    )


@app.route("/health")
def health():
    """Return health check status."""
    return jsonify({"status": "healthy", "environment": app.config["ENV"]})


@app.route("/config")
def get_config():
    """Return non-sensitive configuration information."""
    return jsonify(
        {
            "env": app.config["ENV"],
            "debug": app.config["DEBUG"],
            "version": app.config["VERSION"],
            "database": app.config["DATABASE_URL"].split("@")[0] + "@******",
        }
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
