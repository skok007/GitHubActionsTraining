import json
import os
from datetime import datetime

import pytest


def test_basic_assertion():
    """Basic assertion test"""
    assert True


def test_string_operations():
    """Test string operations"""
    test_string = "Hello, World!"
    assert len(test_string) == 13
    assert test_string.upper() == "HELLO, WORLD!"
    assert test_string.split(",") == ["Hello", " World!"]


def test_file_operations(tmp_path):
    """Test file operations using pytest's tmp_path fixture"""
    # Create a temporary file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")

    # Verify file exists and content
    assert test_file.exists()
    assert test_file.read_text() == "Test content"


def test_json_operations():
    """Test JSON operations"""
    test_data = {"name": "Test", "value": 42, "timestamp": datetime.now().isoformat()}

    # Test JSON serialization
    json_str = json.dumps(test_data)
    assert isinstance(json_str, str)

    # Test JSON deserialization
    parsed_data = json.loads(json_str)
    assert parsed_data["name"] == "Test"
    assert parsed_data["value"] == 42


@pytest.mark.parametrize(
    "input,expected",
    [
        ("test", "test"),
        ("", ""),
        ("hello world", "hello world"),
    ],
)
def test_parametrized(input, expected):
    """Test parametrized test cases"""
    assert input == expected


def test_environment_variables():
    """Test environment variable handling"""
    # Test with default value
    assert os.getenv("NON_EXISTENT_VAR", "default") == "default"

    # Test with actual environment variable
    os.environ["TEST_VAR"] = "test_value"
    assert os.getenv("TEST_VAR") == "test_value"
