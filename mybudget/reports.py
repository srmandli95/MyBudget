from mybudget.models import Budget, Transaction
from mybudget.calculations import calculate_monthly_remaining
from decimal import Decimal
from datetime import date

def format_monthly_report(
    budgets: list[Budget],
    transactions: list[Transaction],
    year: int,
    month: int
) -> str:

    budget_limit = calculate_monthly_remaining(
            budgets, transactions, year, month
        )

    lines = [f"Budget report: {year}-{month:02d}"]

    for budget in budgets:
        lines.append(f"category: {budget.category}")
        lines.append(f"limit: {budget.limit}")
        lines.append(f"remaining: {budget_limit[budget.category]}")

    return "\n".join(lines)

if __name__ == "__main__":
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

    print(format_monthly_report(budgets, transactions, 2026, 10))