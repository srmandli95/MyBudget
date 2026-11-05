from decimal import Decimal
from mybudget.models import Transaction, Budget
from datetime import date
from mybudget.calculations import calculate_monthly_remaining

def generator_calculate_montly_remaining():
    yield Transaction("Groceries", Decimal("10.00"), date(2026, 10, 5))
    yield Transaction("Gas", Decimal("20.00"), date(2026, 10, 5))

transactions = list(generator_calculate_montly_remaining())

budgets = [
    Budget("Groceries", Decimal("100.00")),
    Budget("Gas", Decimal("100.00"))
]


remaining = calculate_monthly_remaining(budgets, transactions , 2026, 10)
print(remaining)