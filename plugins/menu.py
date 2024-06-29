"""
This module provides menu functionalities for the application.
"""

from plugins.plugin_interface import CommandPlugin

class MenuCommand(CommandPlugin):
    """
    MenuCommand provides a list of available commands.
    """

    def execute(self, *args, **kwargs):
        """Execute the menu command."""
        return "Available commands: help, greet, goodbye, exit, menu"

    def get_command_name(self):
        """Return the name of the command."""
        return "menu"
