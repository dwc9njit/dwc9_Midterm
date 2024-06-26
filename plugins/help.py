"""
This module provides help functionalities for the application.
"""

from plugins.command_handler import Command

class HelpCommand(Command):
    """
    Help class provides help text to the users.
    """
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        commands = ", ".join(self.command_handler.commands.keys())
        print(f"Available commands: {commands}")
