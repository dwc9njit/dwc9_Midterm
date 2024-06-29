import os
import sys
from decimal import Decimal, InvalidOperation
from calculator.operations import Calculator

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from command_handler import CommandHandler
from plugins.plugin_manager import PluginManager
from dotenv import load_dotenv
import logging

def calculate_and_print(a_string, b_string, operation_string):
    try:
        a = Decimal(a_string)
        b = Decimal(b_string)
    except InvalidOperation:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        return

    try:
        if operation_string == 'add':
            result = Calculator.add(a, b)
        elif operation_string == 'subtract':
            result = Calculator.subtract(a, b)
        elif operation_string == 'multiply':
            result = Calculator.multiply(a, b)
        elif operation_string == 'divide':
            result = Calculator.divide(a, b)
        elif operation_string == 'exponent':
            result = Calculator.exponent(a, b)
        else:
            print(f"Unknown operation: {operation_string}")
            return
        print(f"The result of {a_string} {operation_string} {b_string} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except Exception as e:
        print(f"Error performing calculation: {e}")

load_dotenv()

class App:
    def __init__(self):
        self.plugin_manager = PluginManager('plugins', command_handler=self)
        self.command_handler = CommandHandler(self.plugin_manager)
        self.running = True

        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)

        api_key = os.getenv('API_KEY')
        self.logger.info(f"API Key Loaded: {api_key}")

    def start(self):
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
            except Exception as e:
                self.logger.error(f"An error occurred: {e}")
                print(f"An error occurred: {e}")

def main():
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
