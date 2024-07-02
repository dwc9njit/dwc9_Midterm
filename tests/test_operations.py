# test_operations.py
'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import Calculator

@pytest.fixture(autouse=True)
def clear_history():
    '''tesing clear historu'''
    Calculations.clear_history()


def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Calculator.add, Decimal('10'), Decimal('5'))
    assert calculation.perform_operation() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Calculator.subtract, Decimal('10'), Decimal('5'))
    assert calculation.perform_operation() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Calculator.multiply, Decimal('10'), Decimal('5'))
    assert calculation.perform_operation() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Calculator.divide, Decimal('10'), Decimal('5'))
    assert calculation.perform_operation() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculation = Calculation(Calculator.divide, Decimal('10'), Decimal('0'))
        calculation.perform_operation()

def test_operation_exponent():
    '''Testing the exponential function'''
    calculation = Calculation(Calculator.exponent, Decimal('2'), Decimal('3'))
    assert calculation.perform_operation() == Decimal("8"), "Exponential operation failed"
