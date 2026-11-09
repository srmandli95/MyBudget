from time import perf_counter
from decimal import Decimal
from mybudget.calculations import calculate_remaining

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = perf_counter() - self.start
        print(f"elapsed time: {self.elapsed:.6f}")
        return False


with Timer():
    remaining = calculate_remaining(
        Decimal("500.00"),
        Decimal("75.00")
    )
    print(remaining)
