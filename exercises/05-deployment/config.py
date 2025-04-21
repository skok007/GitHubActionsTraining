"""
Configuration settings for different environments.
"""

import os


class Config:
    """Base configuration."""

    VERSION = "1.0.0"
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = "development"
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")


class TestingConfig(Config):
    """Testing configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")


class StagingConfig(Config):
    """Staging configuration."""

    ENV = "staging"
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@staging-db/app")


class ProductionConfig(Config):
    """Production configuration."""

    ENV = "production"
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@prod-db/app")


# Configuration dictionary
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
