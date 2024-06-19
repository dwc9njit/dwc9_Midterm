"""
Unit tests for the calculation module.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide, exponent

@pytest.mark.parametrize("operand_a, operand_b, operation_func, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('2'), Decimal('3'), exponent, Decimal('8')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('20'), Decimal('5'), multiply, Decimal('100')),
    (Decimal('20'), Decimal('4'), divide, Decimal('5')),
])
def test_calculation_operations(operand_a, operand_b, operation_func, expected):
    """Test various operations using the Calculation class."""
    calc = Calculation(operation_func, operand_a, operand_b)
    assert calc.perform_operation() == expected, f"Failed {operation_func.__name__} operation with {operand_a} and {operand_b}"

def test_calculation_repr():
    """Test the __repr__ method of the Calculation class."""
    calc = Calculation(add, Decimal('10'), Decimal('5'))
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """Test division by zero handling in the Calculation class."""
    calc = Calculation(divide, Decimal('10'), Decimal('0'))
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.perform_operation()
