from plugins.command_handler import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting...")
        raise SystemExit(0)
