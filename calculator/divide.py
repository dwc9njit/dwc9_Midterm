"""
This module provides the DivideCommand class for performing division.
"""

from plugins.plugin_interface import CommandPlugin

class DivideCommand(CommandPlugin):
    """
    DivideCommand performs division.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the divide command."""
        if operand_b == 0:
            return "An error occurred: Cannot divide by zero"
        return f"The result of {operand_a} divide {operand_b} is equal to {operand_a / operand_b}"

    def get_command_name(self):
        """Return the name of the command."""
        return "divide"

