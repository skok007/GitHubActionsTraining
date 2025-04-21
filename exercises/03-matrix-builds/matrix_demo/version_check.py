"""
Version compatibility checks for the Matrix Demo package.
"""

import platform
import sys


def get_python_version():
    """Return the Python version as a string."""
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_platform_info():
    """Return information about the current platform."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def check_compatibility():
    """Check if the current Python version is compatible with this package."""
    python_version = sys.version_info

    # This package requires Python 3.7 or higher
    if python_version.major < 3 or (
        python_version.major == 3 and python_version.minor < 7
    ):
        return (
            False,
            f"Python {python_version.major}.{python_version.minor} is not supported. Python 3.7+ is required.",
        )

    return True, f"Python {python_version.major}.{python_version.minor} is compatible."


def get_compatibility_info():
    """Return detailed compatibility information."""
    is_compatible, message = check_compatibility()

    return {
        "compatible": is_compatible,
        "message": message,
        "python_version": get_python_version(),
        "platform": get_platform_info(),
    }
