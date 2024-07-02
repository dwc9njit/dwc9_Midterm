"""
Utility functions for tests.

This module provides utility functions to facilitate testing, including functions
for performing operation tests, executing plugin tests, and suppressing output.
"""

import sys
from io import StringIO
from contextlib import contextmanager
import pytest
from calculator.operation_functions import add, subtract, multiply, divide, exponent

operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'exponent': exponent
}

def perform_operation_test(operand_a, operand_b, operation_func, expected):
    """
    Perform the operation test, handling ZeroDivisionError if expected.

    Args:
        operand_a (Decimal): The first operand.
        operand_b (Decimal): The second operand.
        operation_func (callable): The operation function to test.
        expected (Decimal or str): The expected result or "ZeroDivisionError".
    """
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            operation_func(operand_a, operand_b)
    else:
        assert operation_func(operand_a, operand_b) == expected

def execute_plugin_tests(plugins, mock_inputs):
    """
    Helper function to execute plugin tests.

    Args:
        plugins (dict): Dictionary of command plugins.
        mock_inputs (dict): Dictionary of mock inputs for each command.
    """
    for command_name, plugin in plugins.items():
        if command_name in mock_inputs:
            inputs = mock_inputs[command_name]
            if command_name == "exit":
                with pytest.raises(SystemExit):
                    plugin.execute(*inputs)
            else:
                result = plugin.execute(*inputs)
                assert result is not None, f"{command_name} command returned None"
        else:
            if command_name == "exit":
                with pytest.raises(SystemExit):
                    plugin.execute()
            else:
                result = plugin.execute()
                assert result is not None, f"{command_name} command returned None"

@contextmanager
def suppress_output():
    """
    Context manager to suppress stdout and stderr output.

    Usage:
        with suppress_output():
            # Code that produces output
    """
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    try:
        yield
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr

def suppress_output_decorator(func):
    """
    Decorator to suppress stdout and stderr output for a function.

    Args:
        func (callable): The function to wrap.

    Returns:
        callable: The wrapped function.
    """
    def wrapper(*args, **kwargs):
        with suppress_output():
            return func(*args, **kwargs)
    return wrapper
