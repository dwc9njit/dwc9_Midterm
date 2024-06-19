from .command import Command

class CommandHandler:
    def __init__(self):
        """Initialize the command handler with an empty command dictionary."""
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with a given name.

        Args:
            command_name (str): The name of the command.
            command (Command): The command object that implements the Command interface.
        """
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute a command by its name.

        Args:
            command_name (str): The name of the command to execute.
        """
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
