# operations.py

from decimal import Decimal
from typing import Callable
from .calculation import Calculation
from .calculations import Calculations

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def exponent(a: Decimal, b: Decimal) -> Decimal:
    return a ** b

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
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
