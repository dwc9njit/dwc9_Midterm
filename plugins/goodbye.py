# goodbye.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin

class GoodbyeCommand(CommandPlugin):
    """
    Command class represents a generic command.
    """
    def execute(self, *args, **kwargs):
        """Execute the command."""
        return "GoodBye! Thank you for using the calculator app."
    def get_command_name(self):
        """Execute the command."""
        return "goodbye"
    