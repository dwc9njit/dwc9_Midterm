"""
This module provides the SubtractCommand class for performing subtraction.
"""

from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from calculator.operations import Calculator  # Corrected import

class SubtractCommand(CommandPlugin):
    """
    SubtractCommand performs subtraction.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the subtract command."""
        result = Calculator.subtract(Decimal(operand_a), Decimal(operand_b))
#         print(f"SubtractCommand result: {result}")
        return f"The result of {operand_a} subtract {operand_b} is equal to {result}"

    def get_command_name(self):
        """Return the name of the command."""
        return "subtract"
