"""
This module provides the DivideCommand class for performing division.
"""

from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from calculator.operations import Calculator  # Corrected import

class DivideCommand(CommandPlugin):
    """
    DivideCommand performs division.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the divide command."""
        try:
            result = Calculator.divide(Decimal(operand_a), Decimal(operand_b))
        except ZeroDivisionError:
            return "Cannot divide by zero."
#         print(f"DivideCommand result: {result}")
        return f"The result of {operand_a} divide {operand_b} is equal to {result}"

    def get_command_name(self):
        """Return the name of the command."""
        return "divide"
