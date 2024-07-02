# plugins/load_history.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class LoadHistoryCommand(CommandPlugin):
    """LoadHistoryCommand loads the calculation history from a CSV file."""
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager
    
    def execute(self, *args, **kwargs):
        file_path = input("Enter file path to load history: ")
        Calculations.load_history_from_csv(file_path)
        return f"History loaded from {file_path}"

    def get_command_name(self):
        return "load_history"
    