# save_history.py
"""
This module provides a command to save calculation history.
"""

from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class SaveHistoryCommand(CommandPlugin):
    """SaveHistoryCommand saves the calculation history to a CSV file."""

    def __init__(self, plugin_manager):
        """Initialize the command with a plugin manager."""
        self.plugin_manager = plugin_manager

    def execute(self, *args, **kwargs):
        file_path = input("Enter file path to save history (default: data/calculation_history.csv): ") or "data/calculation_history.csv"
#         print(f"Saving history to {file_path}")
        Calculations.save_history_to_csv(file_path)
        return f"History saved to {file_path}"

    def get_command_name(self):
        return "save_history"
