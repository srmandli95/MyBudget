from mybudget.calculations import calculate_remaining
from decimal import Decimal

def announce(operation):
    def wrapper(budget, spent):
        print("Starting calculation")
        result = operation(budget, spent)
        print("Calculation finished")
        return result

    return wrapper

calculate = announce(calculate_remaining)

print(calculate(Decimal("500.00"), Decimal("75.00")))
