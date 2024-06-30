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
                print(f"Command {command_name} executed successfully with result: {result}")
        else:
            if command_name == "exit":
                with pytest.raises(SystemExit):
                    plugin.execute()
            else:
                result = plugin.execute()
                assert result is not None, f"{command_name} command returned None"
                print(f"Command {command_name} executed successfully with result: {result}")
