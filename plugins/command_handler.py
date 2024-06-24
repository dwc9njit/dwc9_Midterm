# plugins/command_handler.py
import logging
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.logger = logging.getLogger(__name__)

    def register_command(self, name, command):
        self.commands[name] = command
        self.logger.info(f"Command registered: {name}")

    def execute_command(self, name):
        if name in self.commands:
            self.logger.info(f"Executing command: {name}")
            return self.commands[name].execute()
        else:
            self.logger.warning(f"Command not found: {name}")
            return "Command not found."

    def get_command(self, name):
        return self.commands.get(name)