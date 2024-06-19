# tests/test_calculations.py

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide, exponent

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(add, Decimal('10'), Decimal('5')))
    Calculations.add_calculation(Calculation(subtract, Decimal('20'), Decimal('3')))
    Calculations.add_calculation(Calculation(multiply, Decimal('2'), Decimal('3')))
    Calculations.add_calculation(Calculation(divide, Decimal('10'), Decimal('2')))
    Calculations.add_calculation(Calculation(exponent, Decimal('2'), Decimal('3')))

def test_add_calculation(setup_calculations):
    calc = Calculation(add, Decimal('2'), Decimal('2'))
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 5, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    latest = Calculations.get_latest()
    assert latest.a == Decimal('2'), "The operand a is incorrect"
    assert latest.b == Decimal('3'), "The operand b is incorrect"
    assert latest.operation.__name__ == exponent.__name__, "The operation is incorrect"

def test_find_by_operation(setup_calculations):
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    assert add_operations[0].operation.__name__ == add.__name__, "Found operation is not 'add'"

    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"
    assert subtract_operations[0].operation.__name__ == subtract.__name__, "Found operation is not 'subtract'"

    multiply_operations = Calculations.find_by_operation("multiply")
    assert len(multiply_operations) == 1, "Did not find the correct number of calculations with multiply operation"
    assert multiply_operations[0].operation.__name__ == multiply.__name__, "Found operation is not 'multiply'"

    divide_operations = Calculations.find_by_operation("divide")
    assert len(divide_operations) == 1, "Did not find the correct number of calculations with divide operation"
    assert divide_operations[0].operation.__name__ == divide.__name__, "Found operation is not 'divide'"

    exponent_operations = Calculations.find_by_operation("exponent")
    assert len(exponent_operations) == 1, "Did not find the correct number of calculations with exponent operation"
    assert exponent_operations[0].operation.__name__ == exponent.__name__, "Found operation is not 'exponent'"
