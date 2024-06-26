# plugins/menu.py
"""
This module provides help functionalities for the application.
"""
from plugins.command_handler import Command

class MenuCommand(Command):
    """
    Command class represents a generic command.
    """

    def execute(self):
        """Execute the command."""
        print("Available commands: help, greet, goodbye, exit, menu")
