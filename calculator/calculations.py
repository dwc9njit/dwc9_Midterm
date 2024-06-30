"""
This module manages a history of calculations.
"""

from typing import List
from .calculation import Calculation

class Calculations:
    """Class managing a history of calculations."""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Add a calculation to the history.
        
        Args:
            calculation (Calculation): The calculation to add.
        """
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
        Return the history of calculations.
        
        Returns:
            List[Calculation]: The list of calculations in history.
        """
        return cls.history

    @classmethod
    def clear_history(cls):
        """
        Clear the history of calculations.
        """
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """
        Get the latest calculation in the history.
        
        Returns:
            Calculation: The latest calculation, or None if history is empty.
        """
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """
        Find calculations by operation name.
        
        Args:
            operation_name (str): The name of the operation to search for.
        
        Returns:
            List[Calculation]: The list of calculations matching the operation name.
        """
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
