# Import necessary modules and classes
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide, exponent  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects
from calculator.commands import CommandHandler
from calculator.commands.exit import ExitCommand
from calculator.commands.goodbye import GoodbyeCommand
from calculator.commands.greet import GreetCommand
from calculator.commands.menu import MenuCommand


class App:
    def __init__(self):
        """Initialize the application with a command handler."""
        self.command_handler = CommandHandler()

    def start(self):
        """Start the application, registering commands and entering the REPL loop."""
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())

        print("Type 'exit' to exit.")
        while True:  # REPL: Read, Evaluate, Print, Loop
            try:
                user_input = input(">>> ").strip()
                self.command_handler.execute_command(user_input)
            except Exception as e:
                print(f"An error occurred: {e}")

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        try:
            if operation == divide and b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            calculation = Calculation.create(a, b, operation)
            Calculations.add_calculation(calculation)
            return calculation.perform()
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
            print(f"Error performing calculation: {e}")
            return Decimal('0')

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)
    
    @staticmethod
    def exponent(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, exponent)
