import os
import pytest

def test_environment_variables():
    """Test environment variable handling"""
    # Set test environment variables
    os.environ["TEST_VAR1"] = "value1"
    os.environ["TEST_VAR2"] = "value2"
    
    # Test getting environment variables
    assert os.getenv("TEST_VAR1") == "value1"
    assert os.getenv("TEST_VAR2") == "value2"
    
    # Test default value for non-existent variable
    assert os.getenv("NON_EXISTENT_VAR", "default") == "default"
    
    # Test environment variable deletion
    del os.environ["TEST_VAR1"]
    assert os.getenv("TEST_VAR1") is None

def test_environment_variable_expansion():
    """Test environment variable expansion"""
    os.environ["BASE_DIR"] = "/home/user"
    os.environ["APP_DIR"] = "${BASE_DIR}/app"
    
    # Test variable expansion
    expanded = os.path.expandvars(os.getenv("APP_DIR"))
    assert expanded == "/home/user/app"

def test_environment_variable_case_sensitivity():
    """Test environment variable case sensitivity"""
    os.environ["UPPERCASE_VAR"] = "UPPER"
    os.environ["lowercase_var"] = "lower"
    
    # Test case sensitivity
    assert os.getenv("UPPERCASE_VAR") == "UPPER"
    assert os.getenv("lowercase_var") == "lower"
    assert os.getenv("LOWERCASE_VAR") is None  # Should be None as environment variables are case-sensitive

@pytest.mark.parametrize("var_name,var_value", [
    ("TEST_INT", "42"),
    ("TEST_FLOAT", "3.14"),
    ("TEST_STRING", "hello"),
    ("TEST_BOOL", "true"),
])
def test_environment_variable_types(var_name, var_value):
    """Test different types of environment variables"""
    os.environ[var_name] = var_value
    assert os.getenv(var_name) == var_value 