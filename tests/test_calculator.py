'''My Calculator Test'''

import pytest
from calculator import App, Calculator

def test_addition():
    '''Test that addition function works'''    
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works'''    
    assert Calculator.subtract(2, 2) == 0

def test_divide():
    '''Test that division function works'''    
    assert Calculator.divide(2, 2) == 1

def test_multiply():
    '''Test that multiply function works'''    
    assert Calculator.multiply(2, 2) == 4

def test_exponent():
    '''Test that exponential function works'''
    assert Calculator.exponent(2, 3) == 8

def test_app_start_exit_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Check the exit code
    assert excinfo.value.code == 0  # Adjust the expected exit code as needed
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
