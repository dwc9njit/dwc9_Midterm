# operation_functions.py
from decimal import Decimal

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
