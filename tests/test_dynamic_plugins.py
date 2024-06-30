"""
Unit tests for dynamically loaded plugins.
"""
import pytest
from plugins.plugin_manager import PluginManager

def test_dynamic_plugins():
    """
    Test all dynamically loaded plugins.
    """
    plugin_manager = PluginManager(['plugins', 'calculator'])
    plugin_manager.load_plugins()
    plugins = plugin_manager.get_all_plugins()

    for command_name, plugin in plugins.items():
        # Prepare mock inputs for commands that require inputs
        mock_inputs = {
            'add': (1, 2),
            'subtract': (5, 3),
            'multiply': (2, 3),
            'divide': (6, 2),
            'exponent': (2, 3),
            'greet': (),
            'goodbye': (),
            'help': (),
            'menu': ()
        }

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
