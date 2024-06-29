# menu.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin

class MenuCommand(CommandPlugin):
    """
    Command class represents a generic command.
    """

    def execute(self):
        """Execute the command."""
        return "Available commands: help, greet, goodbye, exit, menu"

    def get_command_name(self):
        """Return the name of the command."""
        return "menu"
