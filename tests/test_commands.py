"""
This module contains tests for the command handler and commands.
"""

import pytest
from calculator.commands import Command, CommandHandler
from calculator.commands.goodbye import GoodbyeCommand
from calculator.commands.greet import GreetCommand
from calculator.commands.menu import MenuCommand
from calculator.commands.exit import ExitCommand
from calculator import App

class MockCommand(Command):
    """A mock command for testing purposes."""
    def execute(self):
        print("Mock command executed")

def test_greet_command(capfd):
    """Test that the greet command prints 'Hello! How can I help you today?'."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello! How can I help you today?\n", "The GreetCommand should print 'Hello! How can I help you today?'"

def test_goodbye_command(capfd):
    """Test that the goodbye command prints 'Goodbye! Have a nice day!'."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye! Have a nice day!\n", "The GoodbyeCommand should print 'Goodbye! Have a nice day!'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    out, _ = capfd.readouterr()
    assert "Hello! How can I help you today?" in out, "The app did not print the greet message"

def test_command_handler_execution(capfd):
    """Test command handler registration and execution."""
    handler = CommandHandler()
    handler.register_command("greet", GreetCommand())
    handler.register_command("goodbye", GoodbyeCommand())
    handler.register_command("menu", MenuCommand())
    handler.register_command("exit", ExitCommand())

    handler.execute_command("greet")
    out, _ = capfd.readouterr()
    assert "Hello! How can I help you today?" in out

    handler.execute_command("goodbye")
    out, _ = capfd.readouterr()
    assert "Goodbye! Have a nice day!" in out

    handler.execute_command("menu")
    out, _ = capfd.readouterr()
    assert "Menu" in out

    with pytest.raises(SystemExit):
        handler.execute_command("exit")
