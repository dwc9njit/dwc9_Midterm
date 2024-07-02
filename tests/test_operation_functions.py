# test_operation_functions.py
"""
Test module for operation functions in the calculator.

This module tests the basic arithmetic operations: add, subtract, multiply, divide, and exponent.
"""

from decimal import Decimal
import pytest
from calculator.calculations import Calculations
from calculator.operation_functions import add, subtract, multiply, divide, exponent

@pytest.fixture(autouse=True)
def clear_history():
    """
    Fixture to clear the history before each test.
    """
    Calculations.clear_history()

def test_add():
    """
    Test the add function.
    """
    result = add(Decimal(1), Decimal(2))
    assert result == Decimal(3)

def test_subtract():
    """
    Test the subtract function.
    """
    result = subtract(Decimal(5), Decimal(3))
    assert result == Decimal(2)

def test_multiply():
    """
    Test the multiply function.
    """
    result = multiply(Decimal(2), Decimal(3))
    assert result == Decimal(6)

def test_divide():
    """
    Test the divide function.
    """
    result = divide(Decimal(6), Decimal(2))
    assert result == Decimal(3)

def test_divide_by_zero():
    """
    Test the divide function with division by zero.
    """
    with pytest.raises(ZeroDivisionError):
        divide(Decimal(1), Decimal(0))

def test_exponent():
    """
    Test the exponent function.
    """
    result = exponent(Decimal(2), Decimal(3))
    assert result == Decimal(8)
