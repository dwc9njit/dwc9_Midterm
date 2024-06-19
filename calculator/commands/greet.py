from .command import Command

class GreetCommand(Command):
    def execute(self):
        """Print a greeting."""
        print('Hello! How can I help you today?')
