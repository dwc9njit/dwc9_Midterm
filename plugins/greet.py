# greet.py
"""
This module provides help functionalities for the application.
"""
# greet.py
from plugins.plugin_interface import CommandPlugin

class GreetCommand(CommandPlugin):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        return "Hello! Welcome to the calculator app."

    def get_command_name(self):
        """Execute the command."""
        return "greet"

