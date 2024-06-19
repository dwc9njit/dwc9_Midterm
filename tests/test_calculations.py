"""
Unit tests for the calculations module.
"""

from decimal import Decimal
import pytest
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide, exponent

def test_add_calculation():
    """Test adding a calculation to the history."""
    calculation = Calculation(add, Decimal('1'), Decimal('1'))
    Calculations.add_calculation(calculation)
    assert Calculations.get_history()[-1] == calculation, "Failed to add calculation to history."

def test_get_history():
    """Test retrieving the history of calculations."""
    history = Calculations.get_history()
    assert isinstance(history, list), "History is not a list."
    assert all(isinstance(item, Calculation) for item in history), "History does not contain Calculation objects."

def test_clear_history():
    """Test clearing the history of calculations."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "Failed to clear history."

def test_get_latest():
    """Test getting the latest calculation from the history."""
    calculation = Calculation(add, Decimal('1'), Decimal('1'))
    Calculations.add_calculation(calculation)
    assert Calculations.get_latest() == calculation, "Failed to get the latest calculation."

def test_find_by_operation():
    """Test finding calculations by operation."""
    calculation_add = Calculation(add, Decimal('1'), Decimal('1'))
    calculation_subtract = Calculation(subtract, Decimal('2'), Decimal('1'))
    Calculations.add_calculation(calculation_add)
    Calculations.add_calculation(calculation_subtract)
    found_calculations = Calculations.find_by_operation('add')
    assert all(calc.operation.__name__ == 'add' for calc in found_calculations), "Failed to find calculations by operation."

@pytest.mark.parametrize("operation_func, operand_a, operand_b, expected", [
    (multiply, Decimal('2'), Decimal('3'), Decimal('6')),
    (divide, Decimal('10'), Decimal('2'), Decimal('5')),
    (exponent, Decimal('2'), Decimal('3'), Decimal('8'))
])
def test_operations(operation_func, operand_a, operand_b, expected):
    """Test different operations."""
    calculation = Calculation(operation_func, operand_a, operand_b)
    Calculations.add_calculation(calculation)
    assert calculation.perform_operation() == expected, f"Failed {operation_func.__name__} operation with {operand_a} and {operand_b}"
