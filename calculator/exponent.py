"""
This module provides the ExponentCommand class for performing exponentiation.
"""

from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from calculator.operations import Calculator  # Corrected import

class ExponentCommand(CommandPlugin):
    """
    ExponentCommand performs exponentiation.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the exponent command."""
        result = Calculator.exponent(Decimal(operand_a), Decimal(operand_b))
#         print(f"ExponentCommand result: {result}")
        return f"The result of {operand_a} exponent {operand_b} is equal to {result}"

    def get_command_name(self):
        """Return the name of the command."""
        return "exponent"
