"""
This module provides basic arithmetic operations and the Calculator class for performing operations.
"""

from decimal import Decimal
from typing import Callable
from .calculation import Calculation
from .calculations import Calculations

def add(a: Decimal, b: Decimal) -> Decimal:
    """Perform addition of two decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Perform subtraction of two decimal numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Perform multiplication of two decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division of two decimal numbers. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def exponent(a: Decimal, b: Decimal) -> Decimal:
    """Perform exponentiation of two decimal numbers."""
    return a ** b

class Calculator:
    """Class for performing arithmetic operations using the Calculation class."""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Perform the given operation and handle exceptions.
        
        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable[[Decimal, Decimal], Decimal]): The operation function to perform.
        
        Returns:
            Decimal: The result of the operation.
        """
        try:
            calculation = Calculation(operation, a, b)
            Calculations.add_calculation(calculation)
            return calculation.perform_operation()
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
            print(f"Error performing calculation: {e}")
            return Decimal('0')

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition of two decimal numbers."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction of two decimal numbers."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication of two decimal numbers."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division of two decimal numbers."""
        return Calculator._perform_operation(a, b, divide)

    @staticmethod
    def exponent(a: Decimal, b: Decimal) -> Decimal:
        """Perform exponentiation of two decimal numbers."""
        return Calculator._perform_operation(a, b, exponent)
