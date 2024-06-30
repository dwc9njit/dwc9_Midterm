"""
This module provides the ExponentCommand class for performing exponentiation.
"""

from plugins.plugin_interface import CommandPlugin

class ExponentCommand(CommandPlugin):
    """
    ExponentCommand performs exponentiation.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the exponent command."""
        return f"The result of {operand_a} exponent {operand_b} is equal to {operand_a ** operand_b}"

    def get_command_name(self):
        """Return the name of the command."""
        return "exponent"

