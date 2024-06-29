"""
This module contains tests for the command loader.
"""

import unittest
from plugins.plugin_manager import PluginManager
from command_handler import CommandHandler

class TestPluginManager(unittest.TestCase):
    """Unit tests for the PluginManager class."""

    def setUp(self):
        """Set up the test case environment."""
        self.command_handler = CommandHandler(PluginManager('plugins'))

    def test_load_plugins(self):
        """Test that plugins are loaded correctly."""
        self.command_handler.plugin_manager.load_plugins()
        self.assertIn('greet', self.command_handler.plugin_manager.plugins)

    def test_execute_greet_command(self):
        """Test that the 'greet' command executes correctly."""
        self.command_handler.plugin_manager.load_plugins()
        greet_command = self.command_handler.get_command('greet')
        self.assertIsNotNone(greet_command)
        self.assertEqual(greet_command.execute(), "Hello! Welcome to the calculator app.")

if __name__ == '__main__':
    unittest.main()
