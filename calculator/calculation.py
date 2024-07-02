# calculation.py
"""
This module defines the Calculation class for performing arithmetic operations.
"""

from decimal import Decimal
from typing import Callable

class Calculation:
    """Class representing a calculation operation with two operands."""

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

    def perform_operation(self) -> Decimal:
        """
        Perform the operation and return the result.
        
        Returns:
            Decimal: The result of the operation.
        """
        return self.operation(self.a, self.b)

    def __repr__(self):
        """
        Return a string representation of the calculation.
        
        Returns:
            str: String representation of the calculation.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
