from time import perf_counter
from functools import wraps
from decimal import Decimal

def timed(operation):
    @wraps(operation)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try: 
            result = operation(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"{operation.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

@timed
def calculate(budget, spent):
    return budget - spent

print(calculate(Decimal("500.00"), "Two Dollars"))