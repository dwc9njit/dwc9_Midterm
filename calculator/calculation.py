"""
This module defines the Calculation class for performing arithmetic operations.
"""

import logging
from decimal import Decimal
from typing import Callable

class Calculation:
    """
    Class representing a calculation operation with two operands.

    Attributes:
        operation (Callable[[Decimal, Decimal], Decimal]): The operation function to perform.
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        logger (logging.Logger): Logger for this class.
    """

    def __init__(self, operation: Callable[[Decimal, Decimal], Decimal], a: Decimal, b: Decimal):
        """
        Initialize a calculation with the specified operation and operands.

        Args:
            operation (Callable[[Decimal, Decimal], Decimal]): The operation function to perform.
            a (Decimal): The first operand.
            b (Decimal): The second operand.
        """
        self.operation = operation
        self.a = a
        self.b = b
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized Calculation: %s with operands %s and %s", self.operation.__name__, self.a, self.b)

    def perform_operation(self) -> Decimal:
        """
        Perform the operation and return the result.

        Returns:
            Decimal: The result of the operation.
        """
        try:
            result = self.operation(self.a, self.b)
            self.logger.info("Performed operation: %s(%s, %s) = %s", self.operation.__name__, self.a, self.b, result)
            return result
        except Exception as e:
            self.logger.error("Error performing operation %s: %s", self.operation.__name__, e)
            raise

    def __repr__(self):
        """
        Return a string representation of the calculation.

        Returns:
            str: String representation of the calculation.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
