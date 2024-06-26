"""
This module provides help functionalities for the application.
"""
from plugins.command_handler import Command

class ExitCommand(Command):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        print("Exiting...")
        raise SystemExit(0)
