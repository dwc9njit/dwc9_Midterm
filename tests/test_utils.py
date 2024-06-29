"""
Utility functions for tests.
"""

import pytest

def perform_operation_test(operand_a, operand_b, operation_func, expected):
    """Perform the operation test, handling ZeroDivisionError if expected."""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            operation_func(operand_a, operand_b)
    else:
        assert operation_func(operand_a, operand_b) == expected
