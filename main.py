# main.py
"""
Main module for the command-line interface application.
"""

import os
import sys
import logging
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
from plugin_manager import PluginManager
from command_handler import CommandHandler

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

def calculate_and_print(a_string, b_string, operation_string):
    """Calculate and print the result of an arithmetic operation."""
    try:
        a = Decimal(a_string)
        b = Decimal(b_string)
    except InvalidOperation:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        return

    try:
        plugin_manager = PluginManager(['plugins', 'calculator'])
        plugin_manager.load_plugins()  # Ensure plugins are loaded
        operation_plugin = plugin_manager.get_plugin(operation_string)
        if not operation_plugin:
            print(f"Unknown operation: {operation_string}")
            return
        result = operation_plugin.execute(a, b)
        print(f"The result of {a_string} {operation_string} {b_string} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except Exception as e:
        print(f"Error performing calculation: {e}")

class App:
    """Class representing the main application."""

    def __init__(self):
        """Initialize the App."""
        self.plugin_manager = PluginManager(['plugins', 'calculator'])
        self.command_handler = CommandHandler(self.plugin_manager)
        self.running = True

        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)

        api_key = os.getenv('API_KEY')
        self.logger.info("API Key Loaded: %s", api_key)

    def start(self):
        """Start the application and handle user input."""
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
                self.logger.info("Executing command: %s", user_input)
                response = self.command_handler.execute_command(user_input)
                if response:
                    print(response)
            except ZeroDivisionError:
                self.logger.error("An error occurred: Cannot divide by zero")
                print("An error occurred: Cannot divide by zero")
            except Exception as e:
                self.logger.error("An error occurred: %s", e)
                print(f"An error occurred: {e}")

def main():
    """Main entry point for the application."""
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
