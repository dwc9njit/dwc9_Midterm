# view_history.py
"""
This module provides a command to view calculation history.
"""

from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class ViewHistoryCommand(CommandPlugin):
    """Command to view calculation history."""
    def __init__(self, plugin_manager):
        """Execute the view history command."""
        self.plugin_manager = plugin_manager

    def execute(self, *args, **kwargs):
        """Execute the view history command."""
#         print("Executing view_history command.")
        history = Calculations.view_history()
        return history.to_string(index=False)

    def get_command_name(self):
        """Return the name of the command."""
        return "view_history"
