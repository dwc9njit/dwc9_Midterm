# calculation.py

from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, operation: Callable[[Decimal, Decimal], Decimal], a: Decimal, b: Decimal):
        self.operation = operation
        self.a = a
        self.b = b

    def perform_operation(self) -> Decimal:
        return self.operation(self.a, self.b)

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
