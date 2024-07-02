"""
Calculator module that provides basic arithmetic operations.
"""

import logging
import os
from decimal import Decimal
from typing import Callable
from .calculations import Calculations
from .calculation import Calculation
from .operations import add, subtract, multiply, divide, exponent

# Set up logging configuration
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=log_level, format=log_format)

# Create a logger for the calculator package
logger = logging.getLogger(__name__)

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
            logger.info("Performing calculation: %s", calculation)
            Calculations.add_calculation(calculation)
            return result
        except ZeroDivisionError as e:
            logger.error("ZeroDivisionError: %s", e)
            raise e
        except Exception as e:
            logger.error("Error performing calculation: %s", e)
            return Decimal('0')

    @staticmethod
    def perform_operation(operand_a: Decimal, operand_b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Public method to perform an operation."""
        logger.debug("Performing operation with operands: %s, %s and operation: %s", operand_a, operand_b, operation.__name__)
        return Calculator._perform_operation(operand_a, operand_b, operation)

    @staticmethod
    def add(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform addition."""
        logger.info("Addition operation with operands: %s, %s", operand_a, operand_b)
        return Calculator.perform_operation(operand_a, operand_b, add)

    @staticmethod
    def subtract(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform subtraction."""
        logger.info("Subtraction operation with operands: %s, %s", operand_a, operand_b)
        return Calculator.perform_operation(operand_a, operand_b, subtract)

    @staticmethod
    def multiply(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform multiplication."""
        logger.info("Multiplication operation with operands: %s, %s", operand_a, operand_b)
        return Calculator.perform_operation(operand_a, operand_b, multiply)

    @staticmethod
    def divide(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform division."""
        logger.info("Division operation with operands: %s, %s", operand_a, operand_b)
        return Calculator.perform_operation(operand_a, operand_b, divide)
    
    @staticmethod
    def exponent(operand_a: Decimal, operand_b: Decimal) -> Decimal:
        """Perform exponentiation."""
        logger.info("Exponentiation operation with operands: %s, %s", operand_a, operand_b)
        return Calculator.perform_operation(operand_a, operand_b, exponent)
