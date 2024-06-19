from decimal import Decimal
from typing import Callable
from .calculations import Calculations
from .calculation import Calculation
from .operations import add, subtract, multiply, divide, exponent

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        try:
            if operation == Calculator.divide and b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
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
