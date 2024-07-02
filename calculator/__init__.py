# __init__.py
"""
Calculator module that provides basic arithmetic operations.
"""

from decimal import Decimal
from typing import Callable
from .calculations import Calculations
from .calculation import Calculation
from .operations import add, subtract, multiply, divide, exponent

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    @staticmethod
    def _perform_operation(operand_a: Decimal, operand_b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        try:
            if operation == Calculator.divide and operand_b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            calculation = Calculation(operation, operand_a, operand_b)
            result = calculation.perform_operation()
#             print(f"Performing calculation: {calculation}")
            Calculations.add_calculation(calculation)
            return result
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
#             print(f"Error performing calculation: {e}")
            return Decimal('0')

    @staticmethod
    def perform_operation(operand_a: Decimal, operand_b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Public method to perform an operation."""
        return Calculator._perform_operation(operand_a, operand_b, operation)

    @staticmethod
    def add(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform addition."""
        return Calculator.perform_operation(operand_a, operand_b, add)

    @staticmethod
    def subtract(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform subtraction."""
        return Calculator.perform_operation(operand_a, operand_b, subtract)

    @staticmethod
    def multiply(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform multiplication."""
        return Calculator.perform_operation(operand_a, operand_b, multiply)

    @staticmethod
    def divide(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform division."""
        return Calculator.perform_operation(operand_a, operand_b, divide)
    
    @staticmethod
    def exponent(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform exponentiation."""
        return Calculator.perform_operation(operand_a, operand_b, exponent)
