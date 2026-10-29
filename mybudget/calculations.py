from decimal import Decimal
from mybudget.models import Transaction
from datetime import date

def calculate_category_total(transactions: list[Transaction], category: str) -> Decimal:
    total = Decimal("0.0")
    for transaction in transactions:
        if transaction.category == category:
            total += transaction.amount
    return total

def calculate_remaining(budget: Decimal, spent: Decimal):
    
    return budget - spent

def calculate_monthly_category_total(
    transactions: list[Transaction],
    category: str,
    year: int,
    month: int,
) -> Decimal:
    expense = Decimal("0.00")
    for transaction in transactions:
        if transaction.transaction_date.year == year and transaction.transaction_date.month == month and transaction.category == category:
            expense += transaction.amount
    
    return expense


