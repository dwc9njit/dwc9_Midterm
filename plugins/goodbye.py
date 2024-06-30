# goodbye.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin

class GoodbyeCommand(CommandPlugin):
    """
    GoodbyeCommand prints a goodbye message.
    """
    def __init__(self, plugin_manager):
        """Execute the command."""
        self.plugin_manager = plugin_manager

    def execute(self, *args, **kwargs):
        """Execute the goodbye command."""
        return "GoodBye! Thank you for using the calculator app."

    def get_command_name(self):
        """Return the name of the command."""
        return "goodbye"
