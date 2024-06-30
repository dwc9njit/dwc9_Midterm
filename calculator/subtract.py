"""
This module provides the SubtractCommand class for performing subtraction.
"""

from plugins.plugin_interface import CommandPlugin

class SubtractCommand(CommandPlugin):
    """
    SubtractCommand performs subtraction.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the subtract command."""
        return f"The result of {operand_a} subtract {operand_b} is equal to {operand_a - operand_b}"

    def get_command_name(self):
        """Return the name of the command."""
        return "subtract"

