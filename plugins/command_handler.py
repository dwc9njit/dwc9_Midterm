"""
This module handles command execution and registration.
"""

import logging
from abc import ABC, abstractmethod

class Command(ABC):
    """
    Command class represents a generic command.
    """

    @abstractmethod
    def execute(self):
        """Execute the command."""
        raise NotImplementedError("Subclasses should implement this!")

class CommandHandler:
    """
    CommandHandler class manages the registration and execution of commands.
    """

    def __init__(self):
        """Initialize the CommandHandler with an empty command registry."""
        self.commands = {}
        self.logger = logging.getLogger(__name__)

    def register_command(self, name, command):
        """
        Register a command with a given name.

        Args:
            name (str): The name of the command.
            command (Command): The command to register.
        """
        self.commands[name] = command
        self.logger.info("Command registered: %s", name)

    def execute_command(self, name):
        """
        Execute a command by its name.

        Args:
            name (str): The name of the command to execute.
        """
        if name in self.commands:
            self.logger.info("Executing command: %s", name)
            return self.commands[name].execute()
        else:
            self.logger.warning("Command not found: %s", name)
            return "Command not found."

    def get_command(self, name):
        """
        Get a command by its name.

        Args:
            name (str): The name of the command to get.
        """
        return self.commands.get(name)
