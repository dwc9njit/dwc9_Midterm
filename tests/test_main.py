"""
Test suite for main.py to ensure optimal test coverage.
"""

from unittest.mock import patch
import pytest
from main import calculate_and_print, main, App
from plugins.plugin_manager import PluginManager
from command_handler import CommandHandler
from tests.test_utils import execute_plugin_tests  # Ensure this import is correct

def test_calculate_and_print_addition(capsys):
    """
    Test addition operation in calculate_and_print function.
    """
    plugin_manager = PluginManager(['calculator'])
    handler = CommandHandler(plugin_manager)
    handler.plugin_manager.load_plugins()

    calculate_and_print("1", "2", "add")
    captured = capsys.readouterr()
    assert "The result of 1 add 2 is equal to 3" in captured.out

def test_calculate_and_print_invalid_number(capsys):
    """
    Test handling of invalid number input in calculate_and_print function.
    """
    calculate_and_print("one", "2", "add")
    captured = capsys.readouterr()
    assert "Invalid number input: one or 2 is not a valid number." in captured.out

def test_calculate_and_print_unknown_operation(capsys):
    """
    Test handling of unknown operation in calculate_and_print function.
    """
    calculate_and_print("1", "2", "unknown")
    captured = capsys.readouterr()
    assert "Unknown operation: unknown" in captured.out

def test_calculate_and_print_divide_by_zero(capsys):
    """
    Test handling of division by zero in calculate_and_print function.
    """
    plugin_manager = PluginManager(['calculator'])
    handler = CommandHandler(plugin_manager)
    handler.plugin_manager.load_plugins()

    calculate_and_print("1", "0", "divide")
    captured = capsys.readouterr()
    assert "An error occurred: Cannot divide by zero" in captured.out

@patch('builtins.input', side_effect=["exit"])
@patch('main.CommandHandler')
@patch('main.PluginManager')
@patch('main.load_dotenv')
def test_app_start(mock_load_dotenv, mock_plugin_manager, mock_command_handler, mock_input):
    """
    Test the start method of the App class.
    """
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    mock_input.assert_called_once_with(">>> ")
    mock_command_handler().execute_command.assert_any_call('menu')

@patch('sys.argv', ['main.py'])
@patch('builtins.input', side_effect=["exit"])
@patch('main.CommandHandler')
@patch('main.PluginManager')
@patch('main.load_dotenv')
def test_main_no_arguments(mock_load_dotenv, mock_plugin_manager, mock_command_handler, mock_input):
    """
    Test the main function with no command line arguments.
    """
    with pytest.raises(SystemExit):
        main()
    mock_input.assert_called_once_with(">>> ")

@patch('sys.argv', ['main.py', '1', '2', 'add'])
@patch('main.calculate_and_print')
def test_main_with_arguments(mock_calculate_and_print):
    """
    Test the main function with valid command line arguments.
    """
    main()
    mock_calculate_and_print.assert_called_once_with('1', '2', 'add')

@patch('sys.argv', ['main.py', '1', '2'])
@patch('sys.exit')
def test_main_invalid_arguments(mock_sys_exit):
    """
    Test the main function with invalid command line arguments.
    """
    main()
    mock_sys_exit.assert_called_once_with(1)

@patch('builtins.input', side_effect=["greet", "exit"])
@patch('main.CommandHandler')
@patch('main.PluginManager')
@patch('main.load_dotenv')
def test_app_handle_commands(mock_load_dotenv, mock_plugin_manager, mock_command_handler, mock_input):
    """
    Test the handling of commands by the App class.
    """
    mock_command_handler_instance = mock_command_handler.return_value
    mock_command_handler_instance.execute_command.return_value = "Hello!"
    
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    
    assert mock_input.call_count == 2
    mock_command_handler_instance.execute_command.assert_any_call("greet")
    assert "Hello!" in mock_command_handler_instance.execute_command.return_value

def test_dynamic_plugins(loaded_plugins):
    """
    Test all dynamically loaded plugins.
    """
    plugins, mock_inputs = loaded_plugins
    execute_plugin_tests(plugins, mock_inputs)
