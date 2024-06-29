# help.py
"""
This module provides help functionalities for the application.
"""

from plugins.plugin_interface import CommandPlugin

class HelpCommand(CommandPlugin):
    """
    Command class represents a generic command.
    """
    def __init__(self, command_handler=None):
        """Initialize the HelpCommand."""
        self.command_handler = command_handler

    def execute(self, *args, **kwargs):
        """Execute the help command."""
        return 'For help please contact: dwc9@njit.edu'

    def get_command_name(self):
        """Get the command name."""
        return "help"
