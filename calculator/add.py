"""
This module provides the AddCommand class for performing addition.
"""

from plugins.plugin_interface import CommandPlugin

class AddCommand(CommandPlugin):
    """
    AddCommand performs addition.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the add command."""
        return f"The result of {operand_a} add {operand_b} is equal to {operand_a + operand_b}"

    def get_command_name(self):
        """Return the name of the command."""
        return "add"
