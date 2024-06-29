"""
Unit tests for the calculations module.
"""

import pytest
from tests.test_utils import perform_operation_test

@pytest.mark.dynamic_data
def test_operations(operand_a, operand_b, operation_func, expected):
    """Test various operations using dynamic data."""
    perform_operation_test(operand_a, operand_b, operation_func, expected)
