# greet.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin

class GreetCommand(CommandPlugin):
    """
    GreetCommand prints a greeting message.
    """
    def __init__(self, plugin_manager):
        """Execute the command."""
        self.plugin_manager = plugin_manager

    def execute(self, *args, **kwargs):
        """Execute the greet command."""
        return "Hello! Welcome to the calculator app."

    def get_command_name(self):
        """Return the name of the command."""
        return "greet"

