from .command import Command

class MenuCommand(Command):
    def execute(self):
        """Print the menu."""
        print('Menu')
        print('Available commands:')
        print('1. greet - Greet the user')
        print('2. goodbye - Say goodbye')
        print('3. exit - Exit the application')
        print('4. menu - Show this menu')
