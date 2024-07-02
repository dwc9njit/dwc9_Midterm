# test_calculation.py
"""
Unit tests for the calculation module.
"""

import pytest
from calculator.calculations import Calculations
from tests.test_utils import perform_operation_test

@pytest.fixture(autouse=True)
def clear_history():
    '''testing clear history'''
    Calculations.clear_history()


@pytest.mark.dynamic_data
def test_operations(operand_a, operand_b, operation_func, expected):
    """Test various operations using dynamic data."""
    perform_operation_test(operand_a, operand_b, operation_func, expected)
