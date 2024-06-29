"""
Unit tests for the calculation module.
"""

import pytest

@pytest.mark.dynamic_data
def test_operations(operand_a, operand_b, operation_func, expected):
    """Test various operations using dynamic data."""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            operation_func(operand_a, operand_b)
    else:
        assert operation_func(operand_a, operand_b) == expected
