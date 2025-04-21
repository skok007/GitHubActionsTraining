"""
Data processing functions for the Matrix Demo package.

Some of these functions may behave differently across Python versions,
making them good candidates for matrix testing.
"""

import json
import sys
from typing import Any, Dict, List, Union


def process_data(data: Union[Dict[str, Any], List[Any]]) -> Dict[str, Any]:
    """
    Process data and return a summary.

    This function may behave differently across Python versions,
    especially with dictionary ordering and type handling.
    """
    result = {
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "data_type": type(data).__name__,
        "processed": False,
        "summary": {},
    }

    if isinstance(data, dict):
        # Dictionary ordering is guaranteed in Python 3.7+
        result["processed"] = True
        result["summary"] = {
            "keys": list(data.keys()),
            "values": list(data.values()),
            "length": len(data),
        }
    elif isinstance(data, list):
        result["processed"] = True
        result["summary"] = {
            "length": len(data),
            "types": [type(item).__name__ for item in data],
        }

    return result


def serialize_data(data: Any) -> str:
    """
    Serialize data to JSON.

    This function may behave differently across Python versions,
    especially with handling of non-serializable objects.
    """
    try:
        return json.dumps(data, sort_keys=True)
    except TypeError as e:
        return f"Error serializing data: {str(e)}"


def parse_version_specific(version_str: str) -> Dict[str, int]:
    """
    Parse a version string into components.

    This function may behave differently across Python versions,
    especially with string handling and dictionary creation.
    """
    parts = version_str.split(".")
    result = {}

    if len(parts) >= 1:
        result["major"] = int(parts[0])
    if len(parts) >= 2:
        result["minor"] = int(parts[1])
    if len(parts) >= 3:
        result["micro"] = int(parts[2])

    return result
