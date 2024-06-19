from .command import Command

class GoodbyeCommand(Command):
    def execute(self):
        """Print a goodbye message."""
        print('Goodbye! Have a nice day!')
