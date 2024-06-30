"""Test module for conftest.py."""

# pylint: disable=comparison-with-callable, unnecessary-pass

from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, exponent
from tests.conftest import generate_test_data, pytest_generate_tests

@pytest.fixture
def fake():
    """Fixture to initialize Faker."""
    return Faker()

def test_generate_test_data(fake):
    """Test generate_test_data function."""
    num_records = 10
    data = list(generate_test_data(num_records))
    assert len(data) == num_records
    for a, b, operation_func, expected in data:
        assert isinstance(a, Decimal)
        assert isinstance(b, Decimal)
        assert operation_func in [add, subtract, multiply, divide, exponent]
        if operation_func == divide and b == Decimal(0):
            assert expected == "ZeroDivisionError"
        else:
            assert expected == operation_func(a, b)

def test_pytest_addoption(pytestconfig):
    """Test pytest_addoption function."""
    # Check if the --num_records option is set to either the default (5) or the provided value (10)
    num_records = pytestconfig.getoption("--num_records")
    assert num_records in [5, 10]

def test_pytest_generate_tests():
    """Test pytest_generate_tests function."""
    class FakeMetafunc:
        """Fake Metafunc class for testing purposes."""
        def __init__(self):
            self.fixturenames = ["operand_a", "operand_b", "operation_func", "expected"]
            self.config = self.FakeConfig()

        class FakeConfig:
            """Fake Config class for testing purposes."""
            def getoption(self, option_name):
                """Get option method for FakeConfig."""
                if option_name == "num_records":
                    return 5
                return None

        def parametrize(self, *args, **kwargs):
            """Parametrize method for FakeMetafunc."""
            pass

    fake_metafunc = FakeMetafunc()
    pytest_generate_tests(fake_metafunc)

def test_sample_fixture(sample_fixture):
    """Test to ensure sample_fixture is working."""
    assert sample_fixture == "sample data"
