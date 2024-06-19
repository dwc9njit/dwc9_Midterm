import pytest
from decimal import Decimal
from calculator import Calculator
from calculator.operations import Calculator


def test_addition():
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')

def test_subtraction():
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')

def test_divide():
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')

def test_multiply():
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')

def test_exponent():
    assert Calculator.exponent(Decimal('2'), Decimal('3')) == Decimal('8')
