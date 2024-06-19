"""
This module contains tests for the command handler and commands.
"""

import pytest
from commands import Command, CommandHandler
from commands.goodbye import GoodbyeCommand
from commands.greet import GreetCommand
from commands.menu import MenuCommand
from commands.exit import ExitCommand
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
    assert out == "Hello!\n", "The GreetCommand should print 'Hello!'"

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
    assert "Hello!" in out, "The app did not print the greet message"

def test_command_handler_execution(capfd):
    """Test command handler registration and execution."""
    handler = CommandHandler()
    handler.register_command("greet", GreetCommand())
    handler.register_command("goodbye", GoodbyeCommand())
    handler.register_command("menu", MenuCommand())
    handler.register_command("exit", ExitCommand())

    handler.execute_command("greet")
    out, _ = capfd.readouterr()
    assert "Hello!" in out

    handler.execute_command("goodbye")
    out, _ = capfd.readouterr()
    assert "Goodbye!" in out

    handler.execute_command("menu")
    out, _ = capfd.readouterr()
    assert "Available commands: greet, goodbye, exit, menu" in out

    with pytest.raises(SystemExit):
        handler.execute_command("exit")
