import sys
import pytest
from main import main, calculate_and_print, App

def test_calculate_and_print(capsys):
    """Test the calculate_and_print function with various inputs and expected outputs."""
    test_cases = [
        ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
        ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
        ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
        ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
        ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
        ("2", "3", 'exponent', "The result of 2 exponent 3 is equal to 8"),
        ("9", "3", 'unknown', "Unknown operation: unknown"),
        ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
        ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
    ]

    for a_string, b_string, operation_string, expected_string in test_cases:
        calculate_and_print(a_string, b_string, operation_string)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_string, f"Failed on {a_string} {operation_string} {b_string}"

@pytest.mark.timeout(10)
def test_main_no_arguments(monkeypatch, capsys):
    """Test the main function behavior with no arguments provided."""
    
    # Replace sys.argv to simulate no arguments
    monkeypatch.setattr(sys, 'argv', ['main.py'])
    
    # Mock input to simulate the 'exit' command
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit) as e:
        main()
    
    captured = capsys.readouterr()
    expected_output = "Usage: python main.py <number1> <number2> <operation>\nOr run without arguments to enter command mode."
    
    # Check if the output contains the expected usage message and the exit message
    assert expected_output in captured.out.strip()
    assert "Exiting the application." in captured.out.strip()
    assert e.type == SystemExit
    assert e.value.code == 0

def test_main_with_arguments(monkeypatch, capsys):
    """Test the main function behavior with valid arguments provided."""
    monkeypatch.setattr(sys, 'argv', ['main.py', '5', '3', 'add'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 5 add 3 is equal to 8"

def test_main_invalid_operation(monkeypatch, capsys):
    """Test the main function behavior with an invalid operation provided."""
    monkeypatch.setattr(sys, 'argv', ['main.py', '5', '3', 'unknown'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Unknown operation: unknown"

def test_main_invalid_number(monkeypatch, capsys):
    """Test the main function behavior with invalid number input provided."""
    monkeypatch.setattr(sys, 'argv', ['main.py', 'a', '3', 'add'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid number input: a or 3 is not a valid number."

def test_main_division_by_zero(monkeypatch, capsys):
    """Test the main function behavior when division by zero is attempted."""
    monkeypatch.setattr(sys, 'argv', ['main.py', '10', '0', 'divide'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "An error occurred: Cannot divide by zero"

def test_app_exit_command(monkeypatch, capsys):
    """Test the REPL exit command in the App class."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    
    captured = capsys.readouterr()
    assert "Exiting the application." in captured.out
