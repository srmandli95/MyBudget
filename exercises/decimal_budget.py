from decimal import Decimal 

def calculate_remaining(budget: Decimal, spent: Decimal) -> Decimal:
    return budget - spent


print(calculate_remaining(Decimal("500.00"), Decimal("75.25")))
