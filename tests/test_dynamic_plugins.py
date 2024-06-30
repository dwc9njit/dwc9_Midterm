"""
Unit tests for dynamically loaded plugins.
"""
import pytest

def test_dynamic_plugins(loaded_plugins):
    """
    Test all dynamically loaded plugins.
    """
    plugins, mock_inputs = loaded_plugins

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
