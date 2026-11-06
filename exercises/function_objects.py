from mybudget.calculations import calculate_remaining
from decimal import Decimal

operation = calculate_remaining

print(operation is calculate_remaining)

print(operation(Decimal("500.00"), Decimal("75.00")))


def runs_calculations(operation, budget, spent):
    return operation(budget,spent)

result = runs_calculations(
    calculate_remaining,
    Decimal("500.00"),
    Decimal("75.00")
)

print(result)



