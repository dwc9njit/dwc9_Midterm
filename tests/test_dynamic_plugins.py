"""
Unit tests for dynamically loaded plugins.
"""
from tests.test_utils import execute_plugin_tests

def test_dynamic_plugins(loaded_plugins):
    """
    Test all dynamically loaded plugins.
    """
    plugins, mock_inputs = loaded_plugins
    execute_plugin_tests(plugins, mock_inputs)
