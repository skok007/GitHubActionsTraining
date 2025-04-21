"""
Tests for the version_check module.
"""

import sys
from unittest.mock import patch

import pytest
from matrix_demo.version_check import (check_compatibility,
                                       get_compatibility_info,
                                       get_platform_info, get_python_version)


def test_get_python_version():
    """Test that get_python_version returns the correct format."""
    version = get_python_version()
    assert isinstance(version, str)
    assert len(version.split(".")) >= 3


def test_get_platform_info():
    """Test that get_platform_info returns a dictionary with expected keys."""
    info = get_platform_info()
    assert isinstance(info, dict)
    assert "system" in info
    assert "release" in info
    assert "version" in info
    assert "machine" in info
    assert "processor" in info


def test_check_compatibility():
    """Test that check_compatibility returns the expected results."""
    is_compatible, message = check_compatibility()
    assert isinstance(is_compatible, bool)
    assert isinstance(message, str)

    # If running on Python 3.7+, it should be compatible
    if sys.version_info >= (3, 7):
        assert is_compatible is True
        assert "compatible" in message.lower()
    else:
        assert is_compatible is False
        assert "not supported" in message.lower()


def test_check_compatibility_old_version():
    """Test compatibility check with an old Python version."""
    with patch('sys.version_info', type('VersionInfo', (), {'major': 3, 'minor': 6, 'micro': 0})):
        is_compatible, message = check_compatibility()
        assert is_compatible is False
        assert "not supported" in message.lower()
        assert "3.6" in message


def test_get_compatibility_info():
    """Test that get_compatibility_info returns a dictionary with expected keys."""
    info = get_compatibility_info()
    assert isinstance(info, dict)
    assert "compatible" in info
    assert "message" in info
    assert "python_version" in info
    assert "platform" in info
    assert isinstance(info["compatible"], bool)
    assert isinstance(info["message"], str)
    assert isinstance(info["python_version"], str)
    assert isinstance(info["platform"], dict)
