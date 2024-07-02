# test_dynamic_plugins.py

'''Module for testing dynamic plugins'''
from unittest.mock import patch
import pytest
from calculator.calculations import Calculations
from tests.test_utils import execute_plugin_tests

@pytest.fixture(autouse=True)
def clear_history():
    '''testing clear history'''
    Calculations.clear_history()

@patch('builtins.input', side_effect=["0", "0", "0", "0", "exit"])  # Add more values if necessary
def test_dynamic_plugins(mock_input, loaded_plugins):
    """
    Test all dynamically loaded plugins.
    """
    plugins, mock_inputs = loaded_plugins
    execute_plugin_tests(plugins, mock_inputs)
