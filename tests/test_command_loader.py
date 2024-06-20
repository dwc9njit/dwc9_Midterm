"""
This module contains tests for the CommandLoader class.
"""

import unittest
from plugins.command_loader import CommandLoader
from plugins.command_handler import Command

class TestCommandLoader(unittest.TestCase):
    """Test suite for the CommandLoader class."""

    def test_load_plugins(self):
        """Test that plugins are loaded correctly."""
        command_loader = CommandLoader('plugins')
        command_loader.load_plugins()
        self.assertIn('greet', command_loader.commands)

    def test_execute_greet_command(self):
        """Test that the 'greet' command executes correctly."""
        command_loader = CommandLoader('plugins')
        command_loader.load_plugins()
        greet_command = command_loader.get_command('greet')
        self.assertIsNotNone(greet_command)
        self.assertIsInstance(greet_command, Command)
