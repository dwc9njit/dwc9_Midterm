"""
Module for handling commands in the calculator application.

This module defines the CommandHandler class, which manages the registration and
execution of commands using plugins.
"""

import logging
from decimal import Decimal, InvalidOperation
from plugins.plugin_interface import CommandPlugin
from calculator.calculations import Calculations

class CommandHandler:
    """
    Manages the registration and execution of commands.

    Attributes:
        plugin_manager (PluginManager): The plugin manager for handling plugins.
        logger (logging.Logger): Logger for this class.
    """

    def __init__(self, plugin_manager):
        """
        Initialize the CommandHandler with a plugin manager and set up logging.

        Args:
            plugin_manager (PluginManager): The plugin manager to manage command plugins.
        """
        self.plugin_manager = plugin_manager
        self.logger = logging.getLogger(__name__)

    def execute_command(self, name, *args):
        """
        Execute a command by its name with optional arguments.

        Args:
            name (str): The name of the command to execute.
            args (tuple): Additional arguments to pass to the command.

        Returns:
            str: The result of the command execution.
        """
        self.logger.info("Attempting to execute command: %s", name)

        # Handle specific commands directly related to history management
        if name == "view_history":
            self.logger.info("Viewing calculation history.")
            return Calculations.view_history().to_string()
        elif name == "clear_history":
            Calculations.clear_history()
            self.logger.info("Calculation history cleared.")
            return "Calculation history cleared."
        elif name == "delete_history":
            Calculations.delete_history()
            self.logger.info("Calculation history deleted.")
            return "Calculation history deleted."
        elif name == "save_history":
            command = self.plugin_manager.get_plugin(name)
            if command:
                return command.execute()
            else:
                self.logger.warning("Command not found: %s", name)
                return "Command not found."

        # Handle arithmetic commands and other plugins
        command = self.plugin_manager.get_plugin(name)
        if command:
            self.logger.info("Executing command: %s", name)
            try:
                if name in ['add', 'subtract', 'multiply', 'divide', 'exponent']:
                    if len(args) < 2:
                        operand_a = input("Enter first operand: ")
                        operand_b = input("Enter second operand: ")
                        self.logger.info("Operands received: %s, %s", operand_a, operand_b)
                        return command.execute(Decimal(operand_a), Decimal(operand_b))
                    return command.execute(*args)
                else:
                    return command.execute(*args)
            except InvalidOperation:
                self.logger.error("Invalid number input.")
                return "Invalid number input."
            except ZeroDivisionError:
                self.logger.error("An error occurred: Cannot divide by zero.")
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

        Returns:
            CommandPlugin: The command plugin instance if found, else None.
        """
        self.logger.debug("Getting command: %s", name)
        return self.plugin_manager.get_plugin(name)
