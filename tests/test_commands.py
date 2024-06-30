"""
Unit tests for command functionalities.
"""
from plugins.greet import GreetCommand
from plugins.plugin_manager import PluginManager
from command_handler import CommandHandler

def test_greet_command():
    """Test that the greet command returns the correct message."""
    plugin_manager = PluginManager(['plugins'])
    command = GreetCommand(plugin_manager)
    assert command.execute() == "Hello! Welcome to the calculator app."

def test_command_handler_execution():
    """Test command handler registration and execution."""
    plugin_manager = PluginManager(['plugins', 'calculator'])
    handler = CommandHandler(plugin_manager)
    handler.plugin_manager.load_plugins()

    assert handler.execute_command("greet") == "Hello! Welcome to the calculator app."
    assert handler.execute_command("goodbye") == "GoodBye! Thank you for using the calculator app."

    # Dynamically check available commands
    available_commands = handler.execute_command("menu").replace("Available commands:\n", "").split("\n")
    assert "help" in available_commands
    assert "greet" in available_commands
    assert "goodbye" in available_commands
    assert "exit" in available_commands
    assert "menu" in available_commands
    assert "add" in available_commands
    assert "subtract" in available_commands
    assert "multiply" in available_commands
    assert "divide" in available_commands
    assert "exponent" in available_commands
