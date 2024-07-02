"""
This module provides the MultiplyCommand class for performing multiplication.
"""

from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from calculator.operations import Calculator  # Corrected import

class MultiplyCommand(CommandPlugin):
    """
    MultiplyCommand performs multiplication.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the multiply command."""
        result = Calculator.multiply(Decimal(operand_a), Decimal(operand_b))
#         print(f"MultiplyCommand result: {result}")
        return f"The result of {operand_a} multiply {operand_b} is equal to {result}"

    def get_command_name(self):
        """Return the name of the command."""
        return "multiply"
