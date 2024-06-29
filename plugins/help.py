# help.py
"""
This module provides help functionalities for the application.
"""

from plugins.plugin_interface import CommandPlugin

class HelpCommand(CommandPlugin):
    def __init__(self, command_handler=None):
        self.command_handler = command_handler

    def execute(self):
        return 'For help please contact: dwc9@njit.edu'

    def get_command_name(self):
        return "help"



