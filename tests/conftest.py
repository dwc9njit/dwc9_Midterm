# conftest.py
"""
This module sets up fixtures and configurations for pytest.
"""

from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, exponent

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data for the calculator operations.

    Args:
        num_records (int): The number of test records to generate.

    Yields:
        tuple: A tuple containing the operands, operation name, operation function, and expected result.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'exponent': exponent
    }
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 5 != 4 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        if operation_func is divide:
            b = Decimal('1') if b == Decimal('0') else b
        
        try:
            if operation_func is divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Add custom command line options to pytest.

    Args:
        parser (Parser): The command line parser.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate parameterized tests.

    Args:
        metafunc (Metafunc): The test function metafunc object.
    """
    if {"operand_a", "operand_b", "operation_func", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        if "operation_name" in metafunc.fixturenames:
            metafunc.parametrize("operand_a, operand_b, operation_name, expected", modified_parameters)
        else:
            metafunc.parametrize("operand_a, operand_b, operation_func, expected", modified_parameters)
