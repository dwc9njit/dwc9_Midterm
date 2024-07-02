# delete_history.py
"""
This module provides a command to delete the calculation history file.
"""

from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class DeleteHistoryCommand(CommandPlugin):
    """Command to delete the calculation history file."""
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager
    
    def execute(self, *args, **kwargs):
        """Execute the delete history command."""
        Calculations.delete_history()
        return "Calculation history file deleted."

    def get_command_name(self):
        """Return the name of the command."""
        return "delete_history"
