from decimal import Decimal
from functools import wraps

def announce(operation):
    @wraps(operation)
    def wrapper(*args, **kwargs):

        print("Starting operation")
        result = operation(*args, **kwargs)
        print("Finished operation")
        return result

    
    return wrapper

@announce
def calculate(budget, spent):
    """Return the budget after spending."""
    return budget - spent

@announce
def describe_category(category):
    return f"Calculate: {category}"


print(calculate(Decimal("500.00"), spent=Decimal("75.00")))
print(describe_category(category="Groceries"))

print(calculate.__name__)
print(calculate.__doc__)
