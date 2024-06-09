"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division, exponentiation) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise decimal arithmetic, which is especially useful in financial calculations.
# Import pytest for writing test cases.
# Import the Calculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide


def test_calculation_operations(operand_a, operand_b, operation_func, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation_func' parameter) on two Decimal operands ('operand_a' and 'operand_b'),
    and that the result matches the expected outcome.
    
    Parameters:
        operand_a (Decimal): The first operand in the calculation.
        operand_b (Decimal): The second operand in the calculation.
        operation_func (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(operand_a, operand_b, operation_func)  # Create a Calculation instance with the provided operands and operation.
    assert calc.perform() == expected, f"Failed {operation_func.__name__} operation with {operand_a} and {operand_b}"  # Perform the operation and assert that the result matches the expected value.

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
