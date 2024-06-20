# plugins/menu.py
from plugins.command_handler import Command

class MenuCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        print("Available commands: help, greet, goodbye, exit, menu")
