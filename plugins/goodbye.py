from plugins.command_handler import Command

class GoodbyeCommand(Command):
    def execute(self):
        print("Goodbye!")
