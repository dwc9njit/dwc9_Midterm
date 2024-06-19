import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from calculator.commands import CommandHandler, MenuCommand, GreetCommand, GoodbyeCommand, ExitCommand

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

    def start(self):
        """Register commands and start the REPL."""
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())

        print("Type 'exit' to exit.")
        while self.running:
            try:
                user_input = input(">>> ").strip()
                if user_input == "exit":
                    self.running = False
                    print("Exiting the application.")
                    raise SystemExit(0)  # Raise SystemExit with a status code
                self.command_handler.execute_command(user_input)
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    if len(sys.argv) == 1:
        # No arguments provided, print usage message and exit
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        sys.exit(1)  # Exit with status 1 to indicate an error
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
