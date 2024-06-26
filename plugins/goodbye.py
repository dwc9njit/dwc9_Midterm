"""
This module provides help functionalities for the application.
"""
from plugins.command_handler import Command

class GoodbyeCommand(Command):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        print("Goodbye!")
