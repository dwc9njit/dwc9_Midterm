"""
This module provides the Calculator class for performing arithmetic operations
and managing the calculation history.
"""

import logging
from decimal import Decimal
from typing import Callable
from .calculation import Calculation
from .history import Calculations
from .operation_functions import add, subtract, multiply, divide, exponent

class Calculator:
    """
    Class for performing arithmetic operations using the Calculation class.
    """

    logger = logging.getLogger(__name__)

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

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        try:
            Calculator.logger.info("Performing operation: %s(%s, %s)", operation.__name__, a, b)
            calculation = Calculation(operation, a, b)
            result = calculation.perform_operation()
            Calculations.add_calculation(calculation)
            Calculator.logger.info("Operation result: %s", result)
            return result
        except ZeroDivisionError as e:
            Calculator.logger.error("Error performing calculation: %s", e)
            raise e
        except Exception as e:
            Calculator.logger.error("Error performing calculation: %s", e)
            return Decimal('0')

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform addition of two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of the addition.
        """
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform subtraction of two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of the subtraction.
        """
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform multiplication of two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of the multiplication.
        """
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform division of two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of the division.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        return Calculator._perform_operation(a, b, divide)

    @staticmethod
    def exponent(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform exponentiation of two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of the exponentiation.
        """
        return Calculator._perform_operation(a, b, exponent)
