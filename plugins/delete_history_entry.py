# plugins/delete_history_entry.py
"""
This module provides help functionalities for the application.
"""
from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class DeleteHistoryEntryCommand(CommandPlugin):
    """DeleteHistoryEntryCommand deletes a specific entry from the calculation history."""
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager
        
    def execute(self, *args, **kwargs):
        index = int(input("Enter index of history entry to delete: "))
        Calculations.delete_history_entry(index)
        return f"Deleted history entry at index {index}"

    def get_command_name(self):
        return "delete_history_entry"
    