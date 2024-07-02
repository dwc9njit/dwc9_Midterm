"""
Conftest module for setting up pytest configurations and fixtures.

This module sets up configurations and fixtures for pytest, including generating
test data, handling command line options, and preparing mock inputs for plugins.
"""

from decimal import Decimal
import pytest
from faker import Faker
from calculator import divide
from tests.test_utils import operation_dict
from plugin_manager import PluginManager

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data for various operations.

    Args:
        num_records (int): The number of test records to generate.

    Yields:
        tuple: A tuple containing the operands, operation function, and expected result.
    """
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 5 != 4 else Decimal(fake.random_number(digits=1))
        operation_func = fake.random_element(elements=list(operation_dict.values()))

        if operation_func is divide:
            b = Decimal('1') if b == Decimal('0') else b

        try:
            if operation_func is divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_func, expected

def pytest_addoption(parser):
    """
    Add a command line option to specify number of records.

    Args:
        parser (Parser): The parser for command line arguments.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate dynamic tests based on the number of records specified.

    Args:
        metafunc (Metafunc): The metafunc object for generating test functions.
    """
    if metafunc.config.getoption("--num_records"):
        if metafunc.definition.get_closest_marker("dynamic_data"):
            if "operand_a" in metafunc.fixturenames and "operand_b" in metafunc.fixturenames and "operation_func" in metafunc.fixturenames and "expected" in metafunc.fixturenames:
                num_records = int(metafunc.config.getoption("num_records"))
                test_data = list(generate_test_data(num_records))
                metafunc.parametrize("operand_a,operand_b,operation_func,expected", test_data)

@pytest.fixture
def sample_fixture():
    """
    Sample fixture for demonstration purposes.

    Returns:
        str: Sample data.
    """
    return "sample data"

@pytest.fixture(scope="module")
def loaded_plugins():
    """
    Fixture to load all plugins and prepare mock inputs.

    Returns:
        tuple: A tuple containing the plugins and mock inputs.
    """
    plugin_manager = PluginManager(['plugins', 'calculator'])
    plugin_manager.load_plugins()
    plugins = plugin_manager.get_all_plugins()
    
    mock_inputs = {
        'add': (1, 2),
        'subtract': (5, 3),
        'multiply': (2, 3),
        'divide': (6, 2),
        'exponent': (2, 3),
        'greet': (),
        'goodbye': (),
        'help': (),
        'menu': (),
        'exit': ()
    }
    
    return plugins, mock_inputs

def test_sample_fixture(sample_fixture):
    """
    Test to ensure sample_fixture is working.

    Args:
        sample_fixture (str): The sample fixture to test.
    """
    assert sample_fixture == "sample data"
