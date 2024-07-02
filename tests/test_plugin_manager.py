# test_plugin_manager.py
"""
This module contains tests for the command loader.
"""

import unittest
from plugin_manager import PluginManager
from command_handler import CommandHandler

class TestPluginManager(unittest.TestCase):
    """Test cases for the PluginManager class."""

    def setUp(self):
        """Set up the test case environment."""
        self.plugin_manager = PluginManager(['plugins', 'calculator'])
        self.command_handler = CommandHandler(self.plugin_manager)

    def test_load_plugins(self):
        """Test that plugins are loaded correctly."""
        self.plugin_manager.load_plugins()
        self.assertIn('greet', self.plugin_manager.plugins)

    def test_execute_greet_command(self):
        """Test that the 'greet' command executes correctly."""
        self.plugin_manager.load_plugins()
        greet_command = self.command_handler.get_command('greet')
        self.assertIsNotNone(greet_command)
        self.assertEqual(greet_command.execute(), "Hello! Welcome to the calculator app.")

    def _create_plugin_instance(self, cls):
        """
        Create an instance of a plugin class.
    
        Args:
            cls (type): The plugin class to create an instance of.
    
        Returns:
            CommandPlugin: An instance of the plugin class.
        """
        if cls.__name__ == "MenuCommand":
            return cls(self)
        return cls()

if __name__ == '__main__':
    unittest.main()
