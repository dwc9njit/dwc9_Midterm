# plugins/clear_history.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class ClearHistoryCommand(CommandPlugin):
    """ClearHistoryCommand clears the calculation history."""
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager
    
    def execute(self, *args, **kwargs):
        Calculations.clear_history()
        return "History cleared"

    def get_command_name(self):
        return "clear_history"
    