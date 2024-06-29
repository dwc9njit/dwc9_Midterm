from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, exponent

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for various operations."""
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
        operation_func = fake.random_element(elements=list(operation_mappings.values()))

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
    """Add a command line option to specify number of records."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate dynamic tests based on the number of records specified."""
    if metafunc.config.getoption("--num_records"):
        if metafunc.definition.get_closest_marker("dynamic_data"):
            if "operand_a" in metafunc.fixturenames and "operand_b" in metafunc.fixturenames and "operation_func" in metafunc.fixturenames and "expected" in metafunc.fixturenames:
                num_records = int(metafunc.config.getoption("num_records"))
                test_data = list(generate_test_data(num_records))
                metafunc.parametrize("operand_a,operand_b,operation_func,expected", test_data)

@pytest.fixture
def sample_fixture():
    """Sample fixture for demonstration purposes."""
    return "sample data"

def test_sample_fixture(sample_fixture):
    """Test to ensure sample_fixture is working."""
    assert sample_fixture == "sample data"
