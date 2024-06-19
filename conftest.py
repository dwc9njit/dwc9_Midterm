from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, exponent

fake = Faker()

def generate_test_data(num_records):
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
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if "operand_a" in metafunc.fixturenames or "operand_b" in metafunc.fixturenames or "operation_func" in metafunc.fixturenames or "expected" in metafunc.fixturenames:
        return

@pytest.fixture
def sample_fixture():
    return "sample data"

def test_sample_fixture(sample_fixture):
    assert sample_fixture == "sample data"
