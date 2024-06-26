# plugins/greet.py
from plugins.command_handler import Command


class GreetCommand(Command):
    def execute(self):
        print("Hello! Welcome to the calculator app.")
