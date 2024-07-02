"""
This module provides the AddCommand class for performing addition.
"""

from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from calculator.operations import Calculator

class AddCommand(CommandPlugin):
    """
    AddCommand performs addition.
    """
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, operand_a, operand_b):
        """Execute the add command."""
        result = Calculator.add(Decimal(operand_a), Decimal(operand_b))
#         print(f"AddCommand result: {result}")
        return f"The result of {operand_a} add {operand_b} is equal to {result}"

    def get_command_name(self):
        """Return the name of the command."""
        return "add"
