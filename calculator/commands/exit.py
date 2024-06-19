import sys
from .command import Command

class ExitCommand(Command):
    def execute(self):
        """Exit the application."""
        print('Exiting the application.')
        sys.exit(0)
