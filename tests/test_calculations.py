# test_calculations.py
"""
Unit tests for the calculations module.
"""
from decimal import Decimal
import pytest
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide, exponent

@pytest.fixture(autouse=True)
def clear_history():
    '''testing clear history'''
    Calculations.clear_history()

def test_add_calculation():
    '''testing add calculation'''
    calculation = Calculation(add, Decimal('1'), Decimal('1'))
    Calculations.add_calculation(calculation)
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'add'
    assert history.iloc[0]['Operand_A'] == 1.0
    assert history.iloc[0]['Operand_B'] == 1.0
    assert history.iloc[0]['Result'] == 2.0

def test_subtract_calculation():
    '''testing subtract calculation'''
    calculation = Calculation(subtract, Decimal('3'), Decimal('1'))
    Calculations.add_calculation(calculation)
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'subtract'
    assert history.iloc[0]['Operand_A'] == 3.0
    assert history.iloc[0]['Operand_B'] == 1.0
    assert history.iloc[0]['Result'] == 2.0

def test_multiply_calculation():
    '''testing multiply calculation'''
    calculation = Calculation(multiply, Decimal('2'), Decimal('3'))
    Calculations.add_calculation(calculation)
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'multiply'
    assert history.iloc[0]['Operand_A'] == 2.0
    assert history.iloc[0]['Operand_B'] == 3.0
    assert history.iloc[0]['Result'] == 6.0

def test_divide_calculation():
    '''testing divide calculation'''
    calculation = Calculation(divide, Decimal('6'), Decimal('2'))
    Calculations.add_calculation(calculation)
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'divide'
    assert history.iloc[0]['Operand_A'] == 6.0
    assert history.iloc[0]['Operand_B'] == 2.0
    assert history.iloc[0]['Result'] == 3.0

def test_exponent_calculation():
    '''testing exponent calculation'''
    calculation = Calculation(exponent, Decimal('2'), Decimal('3'))
    Calculations.add_calculation(calculation)
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'exponent'
    assert history.iloc[0]['Operand_A'] == 2.0
    assert history.iloc[0]['Operand_B'] == 3.0
    assert history.iloc[0]['Result'] == 8.0

def test_clear_history():
    '''testing clear history'''
    Calculations.clear_history()
    history = Calculations.view_history()
    assert len(history) == 0

def test_delete_history_entry():
    '''testing delete history'''
    calculation = Calculation(add, Decimal('1'), Decimal('1'))
    Calculations.add_calculation(calculation)
    Calculations.delete_history_entry(0)
    history = Calculations.view_history()
    assert len(history) == 0

def test_save_and_load_history():
    '''testing save and load history'''
    calculation = Calculation(add, Decimal('1'), Decimal('1'))
    Calculations.add_calculation(calculation)
    Calculations.save_history_to_csv('test_history.csv')
    Calculations.load_history_from_csv('test_history.csv')
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'add'
    assert history.iloc[0]['Operand_A'] == 1.0
    assert history.iloc[0]['Operand_B'] == 1.0
    assert history.iloc[0]['Result'] == 2.0
