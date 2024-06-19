from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        command = self.commands.get(name)
        if command:
            command.execute()
        else:
            print(f"Unknown command: {name}")

class GreetCommand(Command):
    def execute(self):
        print("Hello!")

class GoodbyeCommand(Command):
    def execute(self):
        print("Goodbye!")

class ExitCommand(Command):
    def execute(self):
        print("Exiting...")
        raise SystemExit(0)

class MenuCommand(Command):
    def execute(self):
        print("Available commands: greet, goodbye, exit, menu")
