from decimal import Decimal
from mybudget.models import Transaction, Budget
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
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    expense = Decimal("0.00")
    for transaction in transactions:
        if transaction.transaction_date.year == year and transaction.transaction_date.month == month and transaction.category == category:
            expense += transaction.amount
    
    return expense


def calculate_monthly_remaining(
    budgets: list[Budget],
    transaction: list[Transaction],
    year: int,
    month: int, 
) -> dict[str, Decimal]:

    remaining_budgets = {}

    for budget in budgets:
        
        expense = calculate_monthly_category_total(transaction, budget.category, year, month)
        remaining_budgets[budget.category] = calculate_remaining(
            budget.limit, expense
        )
    
    return remaining_budgets
    

