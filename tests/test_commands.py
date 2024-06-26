"""
This module contains tests for the command handler and commands.
"""

import pytest
from plugins import Command, CommandHandler
from plugins.goodbye import GoodbyeCommand
from plugins.greet import GreetCommand
from plugins.menu import MenuCommand
from plugins.exit import ExitCommand
from plugins.help import HelpCommand
from main import App

class MockCommand(Command):
    """A mock command for testing purposes."""
    def execute(self):
        print("Mock command executed")

def test_greet_command(capfd):
    """Test that the greet command prints 'Hello!'."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello! Welcome to the calculator app.\n", "The GreetCommand should print 'Hello! Welcome to the calculator app.'"

def test_goodbye_command(capfd):
    """Test that the goodbye command prints 'Goodbye!'."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye!\n", "The GoodbyeCommand should print 'Goodbye!'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    out, _ = capfd.readouterr()
    assert "Hello! Welcome to the calculator app." in out, "The app did not print the greet message"

def test_command_handler_execution(capfd):
    """Test command handler registration and execution."""
    handler = CommandHandler()
    handler.register_command("greet", GreetCommand())
    handler.register_command("goodbye", GoodbyeCommand())
    handler.register_command("menu", MenuCommand())
    handler.register_command("exit", ExitCommand())
    handler.register_command("help", HelpCommand(handler))

    handler.execute_command("greet")
    out, _ = capfd.readouterr()
    assert "Hello! Welcome to the calculator app." in out

    handler.execute_command("goodbye")
    out, _ = capfd.readouterr()
    assert "Goodbye!" in out

    handler.execute_command("menu")
    out, _ = capfd.readouterr()
    assert "Available commands: help, greet, goodbye, exit, menu" in out

    with pytest.raises(SystemExit):
        handler.execute_command("exit")

def test_all_commands_execution(capfd):
    """Test that all registered commands in the CommandHandler can be executed."""
    app = App()
    app.command_loader.load_plugins()  # Ensure plugins are loaded

    expected_outputs = {
        'greet': "Hello! Welcome to the calculator app.\n",
        'goodbye': "Goodbye!\n",
        'menu': "Available commands: help, greet, goodbye, exit, menu\n",
        'help': "Available commands: greet, goodbye, exit, menu, help\n",
        'exit': "Exiting...\n"
    }

    for command_name in app.command_handler.commands:
        handler = app.command_handler
        if command_name == 'exit':
            with pytest.raises(SystemExit):
                handler.execute_command(command_name)
        else:
            handler.execute_command(command_name)
            out, _ = capfd.readouterr()
            if command_name == 'help':
                # Handle multi-line output for 'help' command
                assert 'Available commands' in out, f"Expected 'Available commands' in output but got '{out}'"
            else:
                assert out == expected_outputs[command_name], f"Expected '{expected_outputs[command_name]}' but got '{out}'"
                