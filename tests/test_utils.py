# test_utils.py
"""
Utility functions for tests.
"""
import sys
from io import StringIO
from contextlib import contextmanager
import pytest
from calculator.operations import add, subtract, multiply, divide, exponent

# Operation dictionary to map operation names to their corresponding functions
operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'exponent': exponent
}

def perform_operation_test(operand_a, operand_b, operation_func, expected):
    """Perform the operation test, handling ZeroDivisionError if expected."""
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
#                 print(f"Command {command_name} executed successfully with result: {result}")
        else:
            if command_name == "exit":
                with pytest.raises(SystemExit):
                    plugin.execute()
            else:
                result = plugin.execute()
                assert result is not None, f"{command_name} command returned None"
#                 print(f"Command {command_name} executed successfully with result: {result}")

@contextmanager
def suppress_output():
    """Suppress stdout and stderr output."""
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
    """Decorator to suppress stdout and stderr output for a function."""
    def wrapper(*args, **kwargs):
        '''testing wrapper'''
        with suppress_output():
            return func(*args, **kwargs)
    return wrapper
