# help.py
"""
This module provides help functionalities for the application.
"""

from plugins.plugin_interface import CommandPlugin

class HelpCommand(CommandPlugin):
    """
    HelpCommand provides a help message.
    """
    def __init__(self, plugin_manager):
        """Execute the command."""
        self.plugin_manager = plugin_manager

    def execute(self, *args, **kwargs):
        """Execute the help command."""
        return "For help please contact: support@example.com"

    def get_command_name(self):
        """Return the name of the command."""
        return "help"

