from .command_handler import Command

class GreetCommand(Command):
    def execute(self):
        print("Hello!")
