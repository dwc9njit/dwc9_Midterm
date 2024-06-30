"""
This module provides the MultiplyCommand class for performing multiplication.
"""

from plugins.plugin_interface import CommandPlugin

class MultiplyCommand(CommandPlugin):
    """
    MultiplyCommand performs multiplication.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the multiply command."""
        return f"The result of {operand_a} multiply {operand_b} is equal to {operand_a * operand_b}"

    def get_command_name(self):
        """Return the name of the command."""
        return "multiply"

