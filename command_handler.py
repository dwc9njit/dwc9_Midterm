# command_handler.py
import logging
from plugins.plugin_interface import CommandPlugin

class CommandHandler:
    """
    CommandHandler class manages the registration and execution of commands.
    """

    def __init__(self, plugin_manager):
        """Initialize the CommandHandler with an empty command registry."""
        self.plugin_manager = plugin_manager
        self.logger = logging.getLogger(__name__)

    def execute_command(self, name):
        """
        Execute a command by its name.

        Args:
            name (str): The name of the command to execute.
        """
        command = self.plugin_manager.get_plugin(name)
        if command:
            self.logger.info("Executing command: %s", name)
            return command.execute()
        
        self.logger.warning("Command not found: %s", name)
        return "Command not found."

    def get_command(self, name):
        """
        Get a command by its name.

        Args:
            name (str): The name of the command to get.
        """
        return self.plugin_manager.get_plugin(name)
