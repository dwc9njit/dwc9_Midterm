"""Test module for calculation history and operations."""

from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide, exponent

@pytest.mark.parametrize("operand_a, operand_b, operation_func, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('5'), divide, Decimal('2')),
    (Decimal('2'), Decimal('3'), exponent, Decimal('8')),
    (Decimal('10'), Decimal('0'), divide, "ZeroDivisionError"),
])
def test_operations(operand_a, operand_b, operation_func, expected):
    """Test various operations using dynamic data."""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            operation_func(operand_a, operand_b)
    else:
        assert operation_func(operand_a, operand_b) == expected
