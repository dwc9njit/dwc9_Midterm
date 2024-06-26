# plugins/command_handler.py
"""
This module provides help functionalities for the application.
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
        pass

class CommandHandler:
    """
    Command class represents a generic command.
    """
    def __init__(self):
        """Execute the command."""
        self.commands = {}
        self.logger = logging.getLogger(__name__)

    def register_command(self, name, command):
        """Execute the command."""
        self.commands[name] = command
        self.logger.info(f"Command registered: {name}")

    def execute_command(self, name):
        """Execute the command."""
        if name in self.commands:
            self.logger.info(f"Executing command: {name}")
            return self.commands[name].execute()
        else:
            self.logger.warning(f"Command not found: {name}")
            return "Command not found."

    def get_command(self, name):
        """Execute the command."""
        return self.commands.get(name)
    