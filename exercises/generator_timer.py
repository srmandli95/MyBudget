from contextlib import contextmanager
from time import perf_counter
from decimal import Decimal
from mybudget.calculations import calculate_remaining


@contextmanager
def timer():
    start = perf_counter()
    try:
        yield
    finally:
        elapsed = perf_counter() - start  
        print(elapsed)


with timer():
    remaining = calculate_remaining(
        Decimal("500.00"),
        Decimal("75.00")
    )
    print(remaining)
