# tests/test_simple_calculate_and_print.py

import pytest
from simplified_calculate_and_print import calculate_and_print

def test_calculate_and_print_simple(capsys):
    """Test the calculate_and_print function with a simple case."""
    a_string = "5"
    b_string = "3"
    operation_string = "add"
    expected_output = (
        "Starting calculation\n"
        "Converted inputs: a=5.0, b=3.0\n"
        "Performing addition: 5.0 + 3.0\n"
        "The result of 5 add 3 is equal to 8.0"
    )

    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    print(f"Captured output: {captured.out.strip()}")
    assert captured.out.strip() == expected_output
