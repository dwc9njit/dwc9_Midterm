# test_history.py
"""
Test module for the history functionality of the calculator.

This module tests various operations on the calculation history, including
adding, clearing, deleting, viewing, and saving/loading the history.
"""

import os
from decimal import Decimal
import pytest
from calculator.history import Calculations
from calculator.calculation import Calculation
from calculator.operation_functions import add, subtract, multiply, divide, exponent

@pytest.fixture(autouse=True)
def clear_history():
    """
    Fixture to clear the history before each test.
    """
    Calculations.clear_history()

@pytest.fixture(autouse=True)
def cleanup():
    """
    Fixture to ensure a clean environment before and after each test.
    """
    Calculations.history = Calculations.create_empty_history()
    yield

def test_add_calculation():
    """
    Test adding a calculation to the history.
    """
    calc = Calculation(add, Decimal(1), Decimal(2))
    Calculations.add_calculation(calc)
    history = Calculations.view_history()
    assert not history.empty
    assert len(history) == 1
    assert history.iloc[0]['Result'] == 3.0

def test_subtract_calculation():
    """
    Test subtracting a calculation to the history.
    """
    calc = Calculation(subtract, Decimal(3), Decimal(1))
    Calculations.add_calculation(calc)
    history = Calculations.view_history()
    assert not history.empty
    assert len(history) == 1
    assert history.iloc[0]['Result'] == 2.0

def test_multiply_calculation():
    """
    Test multiplying a calculation to the history.
    """
    calc = Calculation(multiply, Decimal(2), Decimal(3))
    Calculations.add_calculation(calc)
    history = Calculations.view_history()
    assert not history.empty
    assert len(history) == 1
    assert history.iloc[0]['Result'] == 6.0

def test_divide_calculation():
    """
    Test dividing a calculation to the history.
    """
    calc = Calculation(divide, Decimal(6), Decimal(2))
    Calculations.add_calculation(calc)
    history = Calculations.view_history()
    assert not history.empty
    assert len(history) == 1
    assert history.iloc[0]['Result'] == 3.0

def test_exponent_calculation():
    """
    Test exponentiation a calculation to the history.
    """
    calc = Calculation(exponent, Decimal(2), Decimal(3))
    Calculations.add_calculation(calc)
    history = Calculations.view_history()
    assert not history.empty
    assert len(history) == 1
    assert history.iloc[0]['Result'] == 8.0

def test_clear_history():
    """
    Test clearing the calculation history.
    """
    calc = Calculation(add, Decimal(1), Decimal(2))
    Calculations.add_calculation(calc)
    Calculations.clear_history()
    history = Calculations.view_history()
    assert history.empty

def test_delete_history():
    """
    Test deleting the calculation history file.
    """
    calc = Calculation(add, Decimal(1), Decimal(2))
    Calculations.add_calculation(calc)
    Calculations.save_history()
    assert os.path.exists(Calculations.history_file)
    Calculations.delete_history()
    assert not os.path.exists(Calculations.history_file)

def test_view_history():
    """
    Test viewing the calculation history.
    """
    calc = Calculation(add, Decimal(1), Decimal(2))
    Calculations.add_calculation(calc)
    history = Calculations.view_history()
    assert not history.empty
    assert len(history) == 1

def test_get_latest():
    """
    Test retrieving the latest calculation from the history.
    """
    calc1 = Calculation(add, Decimal(1), Decimal(2))
    calc2 = Calculation(subtract, Decimal(3), Decimal(1))
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    latest = Calculations.get_latest()
    assert latest.operation is subtract  # Use 'is' for comparing function references
    assert latest.a == Decimal(3)
    assert latest.b == Decimal(1)

def test_delete_history_entry():
    """
    Test deleting a specific entry from the calculation history.
    """
    calc1 = Calculation(add, Decimal(1), Decimal(2))
    calc2 = Calculation(subtract, Decimal(3), Decimal(1))
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    Calculations.delete_history_entry(0)
    history = Calculations.view_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == 'subtract'

def test_save_and_load_history():
    """
    Test saving and loading the calculation history.
    """
    calc = Calculation(add, Decimal(1), Decimal(2))
    Calculations.add_calculation(calc)
    Calculations.save_history()
    
    # Clear only the in-memory history
    Calculations.history = Calculations.create_empty_history()
    
    Calculations.load_history()
    history = Calculations.view_history()
    assert not history.empty
