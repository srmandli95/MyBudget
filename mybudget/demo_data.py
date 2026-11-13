from mybudget.models import Budget, Transaction
from datetime import date
from decimal import Decimal

def demo_data() -> tuple[list[Budget], list[Transaction]]:
    budgets = [
            Budget("Groceries", Decimal("500.00")),
            Budget("Restaurants", Decimal("200.00")),
            Budget("Gas", Decimal("250.00")),
            Budget("miscellaneous", Decimal("150.00")),
        ]

    t1 = Transaction("Groceries", Decimal("400.00"), date(2026, 10, 5))
    t2 = Transaction("Restaurants", Decimal("100.00"), date(2026, 10, 5))
    t3 = Transaction("Gas", Decimal("200.00"), date(2026, 10, 5))   
    t4 = Transaction("Groceries", Decimal("125.00"), date(2026, 10, 5))

    transactions = [t1, t2, t3, t4]

    return budgets, transactions
