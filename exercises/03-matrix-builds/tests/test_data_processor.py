"""
Tests for the data_processor module.
"""

import pytest
from matrix_demo.data_processor import (parse_version_specific, process_data,
                                        serialize_data)


def test_process_data_dict():
    """Test processing a dictionary."""
    data = {"a": 1, "b": 2, "c": 3}
    result = process_data(data)

    assert result["processed"] is True
    assert result["data_type"] == "dict"
    assert "keys" in result["summary"]
    assert "values" in result["summary"]
    assert "length" in result["summary"]
    assert result["summary"]["length"] == 3


def test_process_data_list():
    """Test processing a list."""
    data = [1, "two", 3.0, True]
    result = process_data(data)

    assert result["processed"] is True
    assert result["data_type"] == "list"
    assert "length" in result["summary"]
    assert "types" in result["summary"]
    assert result["summary"]["length"] == 4
    assert len(result["summary"]["types"]) == 4


def test_process_data_invalid():
    """Test processing an invalid data type."""
    data = 42  # Not a dict or list
    result = process_data(data)

    assert result["processed"] is False
    assert result["data_type"] == "int"


def test_serialize_data():
    """Test serializing data to JSON."""
    data = {"a": 1, "b": 2, "c": 3}
    result = serialize_data(data)

    assert isinstance(result, str)
    assert '"a": 1' in result
    assert '"b": 2' in result
    assert '"c": 3' in result


def test_serialize_data_non_serializable():
    """Test serializing non-serializable data."""

    class NonSerializable:
        pass

    data = NonSerializable()
    result = serialize_data(data)

    assert isinstance(result, str)
    assert "Error serializing data" in result


def test_parse_version_specific():
    """Test parsing a version string."""
    version_str = "3.8.5"
    result = parse_version_specific(version_str)

    assert result["major"] == 3
    assert result["minor"] == 8
    assert result["micro"] == 5


def test_parse_version_specific_incomplete():
    """Test parsing an incomplete version string."""
    version_str = "3.8"
    result = parse_version_specific(version_str)

    assert result["major"] == 3
    assert result["minor"] == 8
    assert "micro" not in result
