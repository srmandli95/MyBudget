from collections.abc import Iterable
from decimal import Decimal
from mybudget.models import Transaction
from datetime import date

def calculate_spending_by_category(
    transactions: Iterable[Transaction],
) -> dict[str, Decimal]:
    total = {}

    for transaction in transactions:
        if transaction.category not in total:
            total[transaction.category] = transaction.amount
        else:
            total[transaction.category] += transaction.amount
    return total

def sample_transactions():

    yield Transaction("Groceries", Decimal("10.00"), date(2026,10,10))
    yield Transaction("Gas", Decimal("20.00"), date(2026,10,21))
    yield Transaction("Groceries", Decimal("5.00"), date(2025, 11,21))


print(calculate_spending_by_category(sample_transactions()))



    