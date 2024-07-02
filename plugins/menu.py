# menu.py
"""
This module provides menu functionalities for the application.
"""

from plugins.plugin_interface import CommandPlugin

class MenuCommand(CommandPlugin):
    """
    MenuCommand provides a list of available commands.
    """

    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def execute(self, *args, **kwargs):
        """Execute the menu command."""
        commands = list(self.plugin_manager.get_all_plugins().keys())
        unique_commands = set(commands + [
            "view_history",
            "clear_history",
            "delete_history",
            "save_history"
        ])
        return "Available commands:\n" + "\n".join(sorted(unique_commands))

    def get_command_name(self):
        """Return the name of the command."""
        return "menu"
