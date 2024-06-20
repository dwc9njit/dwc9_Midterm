import sys
from decimal import Decimal, InvalidOperation
from calculator.operations import Calculator
from plugins.command_handler import CommandHandler
from plugins.command_loader import CommandLoader

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

class App:
    def __init__(self):
        """Constructor"""
        self.command_handler = CommandHandler()
        self.running = True
        self.command_loader = CommandLoader('plugins', self.command_handler)
        self.command_loader.load_plugins()

    def start(self):
        """Start the REPL."""
        print("Type 'exit' to exit.")
        while self.running:
            try:
                print("Waiting for user input...")
                user_input = input(">>> ").strip()
                if user_input == "exit":
                    self.running = False
                    print("Exiting the application.")
                    raise SystemExit(0)  # Raise SystemExit with a status code
                print(f"Executing command: {user_input}")
                response = self.command_handler.execute_command(user_input)
                if response:
                    print(response)
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    if len(sys.argv) == 1:
        # No arguments provided, print usage message and enter command mode
        print("No arguments provided. Entering command mode.")
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        app = App()
        app.start()
    elif len(sys.argv) == 4:
        # Calculation mode
        _, a, b, operation = sys.argv
        calculate_and_print(a, b, operation)
    else:
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        sys.exit(1)  # Exit with status 1 to indicate an error

if __name__ == '__main__':
    main()
