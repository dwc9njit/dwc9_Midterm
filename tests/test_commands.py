"""
This module contains tests for the command handler and commands.
"""
import pytest
from command_handler import CommandHandler
from plugins.plugin_manager import PluginManager
from plugins.goodbye import GoodbyeCommand
from plugins.greet import GreetCommand
from plugins.menu import MenuCommand
from plugins.exit import ExitCommand
from plugins.help import HelpCommand

def test_greet_command():
    """Test that the greet command returns the correct message."""
    command = GreetCommand()
    assert command.execute() == "Hello! Welcome to the calculator app."

def test_goodbye_command():
    """Test that the goodbye command returns the correct message."""
    command = GoodbyeCommand()
    assert command.execute() == "GoodBye! Thank you for using the calculator app."

def test_menu_command():
    """Test that the menu command returns the correct message."""
    command = MenuCommand()
    assert command.execute() == "Available commands: help, greet, goodbye, exit, menu"

def test_help_command():
    """Test that the help command returns the correct message."""
    plugin_manager = PluginManager('plugins')
    command = HelpCommand(plugin_manager)
    assert command.execute() == 'For help please contact: dwc9@njit.edu'

def test_exit_command():
    """Test that the exit command raises SystemExit."""
    command = ExitCommand()
    with pytest.raises(SystemExit):
        command.execute()

def test_command_handler_execution():
    """Test command handler registration and execution."""
    plugin_manager = PluginManager('plugins')
    handler = CommandHandler(plugin_manager)
    handler.plugin_manager.load_plugins()

    assert handler.execute_command("greet") == "Hello! Welcome to the calculator app."
    assert handler.execute_command("goodbye") == "GoodBye! Thank you for using the calculator app."
    assert handler.execute_command("menu") == "Available commands: help, greet, goodbye, exit, menu"
    assert handler.execute_command("help") == 'For help please contact: dwc9@njit.edu'

    with pytest.raises(SystemExit):
        handler.execute_command("exit")
