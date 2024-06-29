# exit.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin

class ExitCommand(CommandPlugin):
    def execute(self):
        print("Exiting...")
        raise SystemExit(0)

    def get_command_name(self):
        return "exit"

