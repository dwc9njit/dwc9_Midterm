"""
This module contains tests for the calculate_and_print function from the main module.

The tests verify the correctness of the calculate_and_print function using various scenarios,
including valid operations, division by zero, unknown operations, and invalid number inputs.
"""

from main import calculate_and_print  # Ensure this import matches your project structure

def test_calculate_and_print(capsys):
    """
    Test the calculate_and_print function with various scenarios.

    Args:
        capsys (CaptureFixture): Pytest fixture to capture system output.

    The test cases cover:
        - Valid operations (add, subtract, multiply, divide, exponent)
        - Division by zero
        - Unknown operations
        - Invalid number inputs
    """
    test_cases = [
        ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
        ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
        ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
        ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
        ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Updated to match the actual error message
        ("2", "3", 'exponent', "The result of 2 exponent 3 is equal to 8"),  # Test for exponentiation
        ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
        ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
        ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
    ]

    for a_string, b_string, operation_string, expected_string in test_cases:
        calculate_and_print(a_string, b_string, operation_string)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_string
