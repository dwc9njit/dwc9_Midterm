# plugins/menu.py
"""
This module provides help functionalities for the application.
"""
from plugins.command_handler import Command

class MenuCommand(Command):
    """
    Command class represents a generic command.
    """
    def __init__(self):
        """Execute the command."""
        raise NotImplementedError("Subclasses should implement this!")

    def execute(self):
        """Execute the command."""
        print("Available commands: help, greet, goodbye, exit, menu")
