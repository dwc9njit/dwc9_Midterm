"""
This module provides help functionalities for the application.
"""

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

    def register_command(self, name, command):
        """Execute the command."""
        self.commands[name] = command

    def execute_command(self, name):
        """Execute the command."""
        command = self.commands.get(name)
        if command:
            command.execute()
        else:
            print(f"Unknown command: {name}")

class GreetCommand(Command):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        print("Hello!")

class GoodbyeCommand(Command):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        print("Goodbye!")

class ExitCommand(Command):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        print("Exiting...")
        raise SystemExit(0)

class MenuCommand(Command):
    """
    Command class represents a generic command.
    """
    def execute(self):
        """Execute the command."""
        print("Available commands: greet, goodbye, exit, menu")
