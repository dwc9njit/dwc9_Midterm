"""
This module defines basic arithmetic operations with logging functionality.
"""

import logging
from decimal import Decimal

# Set up logging configuration
logger = logging.getLogger(__name__)

def add(a: Decimal, b: Decimal) -> Decimal:
    """
    Perform addition of two decimal numbers.

    Args:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

    Returns:
        Decimal: The result of the addition.
    """
    result = a + b
    logger.info("Addition: %s + %s = %s", a, b, result)
    return result

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """
    Perform subtraction of two decimal numbers.

    Args:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

    Returns:
        Decimal: The result of the subtraction.
    """
    result = a - b
    logger.info("Subtraction: %s - %s = %s", a, b, result)
    return result

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """
    Perform multiplication of two decimal numbers.

    Args:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

    Returns:
        Decimal: The result of the multiplication.
    """
    result = a * b
    logger.info("Multiplication: %s * %s = %s", a, b, result)
    return result

def divide(a: Decimal, b: Decimal) -> Decimal:
    """
    Perform division of two decimal numbers. Raises ZeroDivisionError if b is zero.

    Args:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

    Returns:
        Decimal: The result of the division.

    Raises:
        ZeroDivisionError: If the second operand is zero.
    """
    if b == 0:
        logger.error("Division by zero: %s / %s", a, b)
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    logger.info("Division: %s / %s = %s", a, b, result)
    return result

def exponent(a: Decimal, b: Decimal) -> Decimal:
    """
    Perform exponentiation of two decimal numbers.

    Args:
        a (Decimal): The base.
        b (Decimal): The exponent.

    Returns:
        Decimal: The result of the exponentiation.
    """
    result = a ** b
    logger.info("Exponentiation: %s ** %s = %s", a, b, result)
    return result
