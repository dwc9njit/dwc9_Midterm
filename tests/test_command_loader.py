"""
This module contains tests for the command loader.
"""

import unittest
from plugins.command_loader import CommandLoader
from plugins.command_handler import CommandHandler, Command

class TestCommandLoader(unittest.TestCase):
    """Unit tests for the CommandLoader class."""
    
    def setUp(self):
        """Set up the test case environment."""
        self.command_handler = CommandHandler()

    def test_load_plugins(self):
        """Test that plugins are loaded correctly."""
        command_loader = CommandLoader('plugins', self.command_handler)
        command_loader.load_plugins()
        self.assertIn('greet', self.command_handler.commands)

    def test_execute_greet_command(self):
        """Test that the 'greet' command executes correctly."""
        command_loader = CommandLoader('plugins', self.command_handler)
        command_loader.load_plugins()
        greet_command = self.command_handler.get_command('greet')
        self.assertIsNotNone(greet_command)
        self.assertIsInstance(greet_command, Command)
