"""
Unit tests for the Calculator class in the calculator module.

This module tests various arithmetic operations provided by the Calculator class,
including addition, subtraction, multiplication, division, and exponentiation.
"""
from decimal import Decimal
import pytest
from calculator import Calculator


def test_add():
    """
    Test the addition operation of the Calculator.
    """
    result = Calculator.add(Decimal('1'), Decimal('1'))
    assert result == Decimal('2')

def test_subtract():
    """
    Test the subtraction operation of the Calculator.
    """
    result = Calculator.subtract(Decimal('2'), Decimal('1'))
    assert result == Decimal('1')

def test_multiply():
    """
    Test the multiplication operation of the Calculator.
    """
    result = Calculator.multiply(Decimal('2'), Decimal('2'))
    assert result == Decimal('4')

def test_divide():
    """
    Test the division operation of the Calculator.
    """
    result = Calculator.divide(Decimal('4'), Decimal('2'))
    assert result == Decimal('2')

def test_divide_by_zero():
    """
    Test the division operation of the Calculator when dividing by zero.
    Expect a ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal('1'), Decimal('0'))

def test_exponent():
    """
    Test the exponentiation operation of the Calculator.
    """
    result = Calculator.exponent(Decimal('2'), Decimal('3'))
    assert result == Decimal('8')

def test_perform_operation_add():
    """
    Test the perform_operation method of the Calculator with addition.
    """
    result = Calculator.perform_operation(Decimal('1'), Decimal('1'), Calculator.add)
    assert result == Decimal('2')

def test_perform_operation_subtract():
    """
    Test the perform_operation method of the Calculator with subtraction.
    """
    result = Calculator.perform_operation(Decimal('2'), Decimal('1'), Calculator.subtract)
    assert result == Decimal('1')

def test_perform_operation_multiply():
    """
    Test the perform_operation method of the Calculator with multiplication.
    """
    result = Calculator.perform_operation(Decimal('2'), Decimal('2'), Calculator.multiply)
    assert result == Decimal('4')

def test_perform_operation_divide():
    """
    Test the perform_operation method of the Calculator with division.
    """
    result = Calculator.perform_operation(Decimal('4'), Decimal('2'), Calculator.divide)
    assert result == Decimal('2')

def test_perform_operation_divide_by_zero():
    """
    Test the perform_operation method of the Calculator when dividing by zero.
    Expect a ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        Calculator.perform_operation(Decimal('1'), Decimal('0'), Calculator.divide)

def test_perform_operation_exponent():
    """
    Test the perform_operation method of the Calculator with exponentiation.
    """
    result = Calculator.perform_operation(Decimal('2'), Decimal('3'), Calculator.exponent)
    assert result == Decimal('8')
