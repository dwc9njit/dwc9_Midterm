"""
Main module for the command-line interface application.

This module serves as the entry point for the CLI application, initializing and
starting the application, handling user input, and performing arithmetic calculations.
"""

import os
import sys
import logging
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
from plugin_manager import PluginManager
from command_handler import CommandHandler
from logging_config import setup_logging

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

def calculate_and_print(a_string, b_string, operation_string):
    """
    Calculate and print the result of an arithmetic operation.

    Args:
        a_string (str): The first operand as a string.
        b_string (str): The second operand as a string.
        operation_string (str): The operation to perform as a string.

    Logs:
        INFO: When a calculation is initiated and when the result is obtained.
        WARNING: When an unknown operation is provided.
        ERROR: When invalid number inputs are provided or a division by zero occurs.
    """
    logger.info(f"Calculating: {a_string} {operation_string} {b_string}")
    try:
        a = Decimal(a_string)
        b = Decimal(b_string)
    except InvalidOperation:
        logger.error(f"Invalid number input: {a_string} or {b_string}")
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        return

    try:
        plugin_manager = PluginManager(['plugins', 'calculator'])
        plugin_manager.load_plugins()  # Ensure plugins are loaded
        operation_plugin = plugin_manager.get_plugin(operation_string)
        if not operation_plugin:
            logger.warning(f"Unknown operation: {operation_string}")
            print(f"Unknown operation: {operation_string}")
            return
        result = operation_plugin.execute(a, b)
        logger.info(f"Result: {result}")
        print(f"The result of {a_string} {operation_string} {b_string} is equal to {result}")
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        print("An error occurred: Cannot divide by zero")
    except Exception as e:
        logger.exception("Error performing calculation")
        print(f"Error performing calculation: {e}")

class App:
    """
    Class representing the main application.

    Attributes:
        plugin_manager (PluginManager): Manages the loading and execution of plugins.
        command_handler (CommandHandler): Handles the execution of commands.
        running (bool): Indicates if the application is running.
        logger (logging.Logger): Logger for the application.
    """

    def __init__(self):
        """Initialize the App."""
        self.plugin_manager = PluginManager(['plugins', 'calculator'])
        self.command_handler = CommandHandler(self.plugin_manager)
        self.running = True

        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)

        api_key = os.getenv('API_KEY')
        self.logger.info("API Key Loaded")

    def start(self):
        """
        Start the application and handle user input.

        Logs:
            INFO: When the application starts, executes a command, and exits.
            ERROR: When a division by zero or other exception occurs.
        """
        self.logger.info("Starting the application")

        # Execute the 'menu' command on start
        print(self.command_handler.execute_command('menu'))

        print("Type 'exit' to exit.")
        while self.running:
            try:
                print("Waiting for user input...")
                user_input = input(">>> ").strip()
                if user_input == "exit":
                    self.running = False
                    print("Exiting the application.")
                    self.logger.info("Exiting the application")
                    raise SystemExit(0)
                self.logger.info(f"Executing command: {user_input}")
                response = self.command_handler.execute_command(user_input)
                if response:
                    print(response)
            except ZeroDivisionError:
                self.logger.error("An error occurred: Cannot divide by zero")
                print("An error occurred: Cannot divide by zero")
            except Exception as e:
                self.logger.exception("An error occurred")
                print(f"An error occurred: {e}")

def main():
    """
    Main entry point for the application.

    Handles command-line arguments and starts the application in either command mode or argument mode.
    """
    if len(sys.argv) == 1:
        print("No arguments provided. Entering command mode.")
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        app = App()
        app.start()
    elif len(sys.argv) == 4:
        _, a, b, operation = sys.argv
        calculate_and_print(a, b, operation)
    else:
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        sys.exit(1)

if __name__ == '__main__':
    main()
