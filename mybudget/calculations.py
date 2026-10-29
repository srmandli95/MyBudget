from decimal import Decimal
from mybudget.models import Transaction

def calculate_category_total(transactions: list[Transaction], category: str) -> Decimal:
    total = Decimal("0.0")
    for transaction in transactions:
        if transaction.category == category:
            total += transaction.amount
    return total