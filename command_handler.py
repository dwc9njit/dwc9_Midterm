# command_handler.py
import logging
from plugins.plugin_interface import CommandPlugin
from decimal import Decimal, InvalidOperation

class CommandHandler:
    """
    CommandHandler class manages the registration and execution of commands.
    """

    def __init__(self, plugin_manager):
        """Initialize the CommandHandler with an empty command registry."""
        self.plugin_manager = plugin_manager
        self.logger = logging.getLogger(__name__)

    def execute_command(self, name, *args):
        """
        Execute a command by its name.

        Args:
            name (str): The name of the command to execute.
            args (tuple): Additional arguments to pass to the command.
        """
        command = self.plugin_manager.get_plugin(name)
        if command:
            self.logger.info("Executing command: %s", name)
            try:
                if name in ['add', 'subtract', 'multiply', 'divide', 'exponent']:
                    if len(args) < 2:
                        operand_a = input("Enter first operand: ")
                        operand_b = input("Enter second operand: ")
                        return command.execute(Decimal(operand_a), Decimal(operand_b))
                    return command.execute(*args)
                else:
                    return command.execute(*args)
            except InvalidOperation:
                return "Invalid number input."
            except ZeroDivisionError:
                return "An error occurred: Cannot divide by zero."
            except Exception as e:
                self.logger.error("Error executing command %s: %s", name, e)
                return f"Error executing command {name}: {e}"

        self.logger.warning("Command not found: %s", name)
        return "Command not found."

    def get_command(self, name):
        """
        Get a command by its name.

        Args:
            name (str): The name of the command to get.
        """
        return self.plugin_manager.get_plugin(name)
