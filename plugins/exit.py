# exit.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin

class ExitCommand(CommandPlugin):
    """
    Command class represents a generic command.
    """
    def execute(self, *args, **kwargs):
        """Execute the command."""
        print("Exiting...")
        raise SystemExit(0)

    def get_command_name(self):
        """Execute the command."""
        return "exit"
